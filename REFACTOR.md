# Tikwizer Refactoring Notes

This document captures all architectural knowledge, connections, quirks, inconsistencies, and technical debt discovered while working on the codebase. Use it as a reference when planning future refactoring work.

---

## 1. How The System Works End-to-End

### The Full Data Pipeline

```
Backend API (GET /api/templates/blocks)
  ↓ returns categories + blocks + default_params from input.json files
BlockPalette (frontend) converts to PaletteBlock with nodeType from CATEGORY_NODE_TYPE map
  ↓ user drags block onto canvas
Canvas.onDrop() creates React Flow node with { id: uid(), data: { block_name_mql, params: default_params, ... } }
  ↓ editorStore.addNode() assigns sequential id_by_user
User configures params via ConfigPanel → BuySellConfig / ConditionConfig / GenericConfig
  ↓
serializeStrategy() in lib/serializer.ts reads both stores (editorStore + strategyStore)
  ↓ maps nodes/edges for all 6 events, attaches variables/constants/project_options
generateMql() wraps in { data: strategy } and POSTs to /api/generate
  ↓
generation_service.py receives it, passes to mql_generator.generate_mql()
  ↓
adapter.refactor(data_raw) transforms the data:
  1. sort_data() — sorts ALL dict keys by length (workaround for string .replace() collisions)
  2. correct_enabled() — ensures every node has enabled=True
  3. enum_check() — moves type=="enum" constants to variables
  4. For each event:
     a. overwrite_ids() — replaces UUID strings with sequential integer indices
     b. create_specific_input() — adds generator-specific params based on block_name_mql
     c. correct_block_names_mql() — maps frontend names to generator template names
     d. set_blocks_input_dic() — builds graph navigation (nexts_true/false, prevs_true/false)
     e. params_fill() — loads input.json defaults for any missing params
     f. manage_extra_double_quotation() — wraps string values in escaped MQL4 quotes
  ↓
ExpertBuilder(data_refactored).process_input() assembles the MQL4 file:
  - Header, system constants, user constants/variables, class blueprints
  - For each event: task elements (from template JSON files), block instances, event handler code
  - Template files are in contents/tasks/{category}/{block_name_mql}/ with 5-6 JSON parts each
  ↓
Returns complete .mq4 string
```

### The Template Replacement System

Every MQL4 template file uses `key_val` placeholders (e.g., `symbol_val`, `stoploss_val`). The code does Python string `.replace(key + "_val", actual_value)` for each parameter key. This is the **single most important architectural decision** in the generator and the source of the most workarounds:

- **`sort_data()` exists** because if you have both `shift` and `ma_shift` as params, replacing `shift_val` first would corrupt `ma_shift_val`. Sorting by key length (longest first) prevents this.
- **The hardcoded 130-key list in `manage_extra_double_quotation()`** exists because `.replace()` has no type awareness — string values need MQL4 quotes added manually.
- **No escaping or delimiters** — if a param value happens to contain `_val` or another key name, it can be incorrectly substituted.

---

## 2. Critical Mappings & Connections

### block_name_mql → Template Directory

The path is: `contents/tasks/{category}/{block_name_mql}/`

But the adapter's `correct_block_names_mql()` consolidates BEFORE this lookup:

| Frontend block_name_mql | Generator template name | Notes |
|-------------------------|------------------------|-------|
| `buy_now` | `buy_sell` | `order_type` set to `ORDER_BUY` by `create_specific_input()` |
| `sell_now` | `buy_sell` | `order_type` set to `ORDER_SELL` |
| `buy_pending_order` | `buy_sell` | `order_type` set to `ORDER_BUY_PENDING` |
| `sell_pending_order` | `buy_sell` | `order_type` set to `ORDER_SELL_PENDING` |
| `condition` | `condition_1_normal` or `condition_1_cross` | Based on operator containing `×` |
| `check_trades_count` | `check_trades_orders_count` | |
| `if_trade` | `check_trades_orders_count` | count_limit=0, operator=">" added |
| `no_trade` | `check_trades_orders_count` | count_limit=0, operator="==" added |
| `if_pending_order` | `check_trades_orders_count` | Similar pattern |
| `no_pending_order` | `check_trades_orders_count` | Similar pattern |
| `no_trade_nearby` | `no_trade_order_nearby` | |
| `no_pending_order_nearby` | `no_trade_order_nearby` | |
| `turn_on_blocks` | `blocks_on_off` | `what` set to `BLOCK_STATE_ENABLE` |
| `turn_off_blocks` | `blocks_on_off` | `what` set to `BLOCK_STATE_DISABLE` |
| `toggle_blocks` | `blocks_on_off` | `what` set to `BLOCK_STATE_TOGGLE` |

### Category → Node Type Mapping (Frontend)

Hardcoded in `BlockPalette.tsx` as `CATEGORY_NODE_TYPE`:

| Backend Category | Frontend Node Type |
|------------------|--------------------|
| `condition_formula` | `conditionNode` |
| `buy_sell` | `actionNode` |
| `trading_actions` | `actionNode` |
| `trailing_stop_break_even` | `actionNode` |
| `time_filters` | `filterNode` |
| `various_signals` | `filterNode` |
| `on_trade_filter_specific_event` | `filterNode` |
| `on_chart_filter_specific_event` | `filterNode` |
| `on_timer_filter_specific_event` | `filterNode` |
| `loop_for_trades_orders` | `loopNode` |
| `loop_for_chart_objects` | `loopNode` |
| `check_trades_orders_count` | `conditionNode` |
| `check_trading_conditions` | `conditionNode` |
| `controlling_blocks` | `controlNode` |
| `output_communication` | `actionNode` |
| `chart_objects` | `actionNode` |
| `modify_variables` | `actionNode` |
| `various_actions` | `actionNode` |

If a new backend category isn't listed here, it silently falls back to `controlNode`.

### Category → Event Restriction

Hardcoded in `BlockPalette.tsx` as `CATEGORY_EVENT_RESTRICTION`:

| Category | Allowed Events |
|----------|---------------|
| `on_trade_filter_specific_event` | `on_trade` only |
| `on_chart_filter_specific_event` | `on_chart` only |
| `on_timer_filter_specific_event` | `on_timer` only |
| `buy_sell` | `on_tick` only |
| `trading_actions` | `on_tick` only |
| `trailing_stop_break_even` | `on_tick` only |
| `loop_for_trades_orders` | `on_tick`, `on_trade` |
| `check_trades_orders_count` | `on_tick`, `on_trade` |
| `check_trading_conditions` | `on_tick`, `on_trade` |
| `loop_for_chart_objects` | `on_tick`, `on_chart` |
| `chart_objects` | `on_tick`, `on_chart` |

Categories not listed are shown in ALL event tabs.

### Edge Color → Flow Path

- `sourceHandle: "blue"` = true/pass path (`nexts_true`, `prevs_true` in generator)
- `sourceHandle: "red"` = false/fail path (`nexts_false`, `prevs_false` in generator)
- `targetHandle` is always `"c"` (center input)

### Event Name → MQL4 Constant

Set in `adapter.py` `set_blocks_input_dic()`:

| Frontend Event | MQL4 Constant |
|---------------|---------------|
| `on_init` | `EVENT_ON_INIT` |
| `on_timer` | `EVENT_ON_TIMER` |
| `on_tick` | `EVENT_ON_TICK` |
| `on_trade` | `EVENT_ON_TRADE` |
| `on_chart` | `EVENT_ON_CHART_EVENT` |
| `on_deinit` | `EVENT_ON_DEINIT` |

---

## 3. Field Name Inconsistencies

### Parameter Naming Chaos

The codebase has no consistent naming convention for parameters. The `input.json` files use a mix:

| Style | Examples | Where |
|-------|----------|-------|
| snake_case | `symbol_mode`, `group_mode`, `how_much_volume`, `stop_loss_mode` | Most task blocks |
| camelCase | `stoploss`, `takeprofit`, `slippage` (flat lowercase) | buy_sell |
| PascalCase | `TrailingStopMode`, `TrailingStartMode`, `CheckBuyOrSell`, `DirectionMode` | trailing, loop blocks |
| Mixed | `Id_user`, `ModeOutput`, `PipsAwayReferencePrice` | various |

This means any frontend component that manually names fields (like BuySellConfig) must use the exact casing from the backend's `input.json`, NOT a normalized version.

### Frontend Field Names That MUST Match Backend

The serializer (`lib/serializer.ts`) passes `node.data.params` straight through to the backend with ZERO transformation. Whatever field names exist in the frontend params dict arrive at the backend unchanged. The adapter then:
1. Fills missing params from `input.json` defaults
2. Does NOT rename any params

So if the frontend stores `lot_size` but the backend expects `how_much_volume`, the backend will have BOTH (the frontend's `lot_size` ignored, and a default `how_much_volume` filled in). This was the original BuySellConfig bug — it used wrong field names (`lot_size`, `stop_loss`, `take_profit`) that didn't match the backend's real field names (`how_much_volume`, `stoploss`, `takeprofit`).

### The Test Fixture Is Wrong

`backend/tests/conftest.py` uses stale field names (`lot_size`, `stop_loss`, `take_profit`, `money_management: "fixed_lot"`) that don't match what the frontend actually sends or what `input.json` defines. These tests pass only because `params_fill()` overwrites with defaults, masking the mismatch.

---

## 4. The Two-Store Architecture

### editorStore (nodes, edges, visual state)

- Owns: `eventGraphs` (6 events × {nodes, edges}), `activeEvent`, `selectedNodeId`, `nextIdByUser`, `clipboard`
- Every mutation spreads the entire `eventGraphs` record — verbose and repetitive
- `nodes()` and `edges()` are getter methods, not derived selectors
- `nextIdByUser` auto-increments but is NEVER reset when loading a strategy (risk of ID collisions)
- Edge IDs: `Date.now()` in `onConnect` but `uid()` in duplicate/paste — inconsistent

### strategyStore (strategy metadata)

- Owns: `name`, `variables[]`, `constants[]`, `projectOptions`, `selectedVarConst`
- No validation on variable/constant names (duplicates allowed)
- `ProjectOptions` uses Python-style string booleans (`'True'`/`'False'`) not JS booleans
- `defaultProjectOptions` hardcodes pip_size rules as a multi-line string

### Cross-Store Coordination

Neither store references the other. All coordination is ad-hoc in UI components:
- **Canvas.tsx**: `onPaneClick` clears both `selectedNodeId` and `selectVarConst(null)`. `onNodeClick` clears `selectVarConst(null)`.
- **BlockPalette.tsx**: Clicking a variable/constant clears `setSelectedNode(null)` in editorStore.
- **AppLayout.tsx**: Conditionally shows ConfigPanel vs VariablesPanel based on both stores' selection state.

**Refactoring opportunity**: Create a single `selectionStore` or a coordination function that enforces mutual exclusion in one place.

---

## 5. The Condition Node's Special Structure

Condition nodes have deeply nested params:

```json
{
  "operator": { "label": ">" },
  "left": {
    "row1": "indicator",
    "row2": "rsi",
    "params": { "period": "14", "applied_price": "PRICE_CLOSE", "shift": "0", "Symbol": "", "Period": "PERIOD_CURRENT" }
  },
  "right": {
    "row1": "value",
    "row2": "Numeric",
    "params": { "value": "70" }
  }
}
```

- `operator.label` is a nested object, not a string — the backend reads `params.get("operator").get("label")`
- `left`/`right` each have `row1` (category: indicator/value/candle/market-properties/account), `row2` (specific type), `params` (type-specific config)
- `GenericConfig` filters out objects (`typeof v !== 'object'`), so condition params are invisible there — only `ConditionConfig` handles them
- The value fetch system in the backend dispatches on `row1` to create different MQL4 class instances

### Indicator Params Are Incomplete in the UI

`IndicatorSelector.tsx` only shows 5 generic params (period, applied_price, shift, Symbol, timeframe). But many indicators need unique params:
- Bollinger Bands: `deviation`, `bands_shift`
- MACD: `fast_ema_period`, `slow_ema_period`, `signal_period`
- Stochastic: `k_period`, `d_period`, `slowing`, `method`, `price_field`
- Alligator: `jaw_period`, `jaw_shift`, `teeth_period`, `teeth_shift`, `lips_period`, `lips_shift`, `ma_method`
- Ichimoku: `tenkan_sen`, `kijun_sen`, `senkou_span_b`

Each indicator's `input.json` in `contents/indicators/{name}/` defines its full param set. The IndicatorSelector should load these dynamically.

### The INDICATORS List Is Hardcoded

`IndicatorSelector.tsx` hardcodes 31 indicators. The backend has these in `contents/indicators/` and they could be loaded dynamically via `GET /api/templates/indicators`.

---

## 6. The Variable Reference System (@prefix)

- Any param field value can start with `@` to reference a variable or constant by name (e.g., `@lot`)
- `ParamInput.tsx` displays these as styled pills with CONST/VAR badges
- Type checking: numeric fields (value looks like a number) allow int/double vars, boolean fields allow bool vars, string fields allow string vars
- The `{x}` button opens a filtered dropdown showing only compatible variables/constants

### What Happens at Generation Time

**Currently unclear / not fully implemented**: The backend's `adapter.py` has `is_not_const_var()` which checks if a value matches a constant or variable name. If it does, the value is NOT wrapped in MQL4 string quotes (it's treated as a variable reference in the generated code). The `@` prefix is a frontend-only convention — it's unclear whether the serializer strips the `@` before sending to the backend, or if the backend handles it.

**Refactoring concern**: The `@` prefix needs to be stripped or translated before generation. The backend expects raw variable names (not prefixed). The serializer currently does NO transformation on param values.

---

## 7. Backend Technical Debt

### String-Based Templating (.replace() everywhere)

This is the root cause of:
- `sort_data()` hack (sorting ALL data keys by length to prevent partial replacements)
- The 130-key hardcoded list in `manage_extra_double_quotation()` for string quoting
- No type awareness — template system doesn't know if a value is a string, number, or enum

**Refactoring approach**: Replace `.replace()` with a proper templating engine (Jinja2, Mustache, or at minimum use delimited placeholders like `{{key}}` instead of `key_val`).

### No Caching

- JSON template files (`input.json`, `class_template.json`, etc.) are re-read from disk on every generation request AND every API call
- `templates.py` rescans the filesystem on every `GET /api/templates/blocks` call
- `adapter.py` `params_fill()` loads `input.json` for every node in every generation

**Refactoring approach**: Cache template files at startup. They never change at runtime.

### Massive Code Duplication in ExpertBuilder

- `phone_notification()`, `alert_message()`, `comment()` each have 8-10 nearly identical blocks for `value_1` through `value_8/10`
- `draw_shape()`, `draw_line()`, `draw_text()`, `move()` repeat the same pattern for `time_1/2/3` and `price_1/2/3`
- Every event handler (`process_blocks_tick/chart/trade/timer/deinit/init`) follows the same structure

**Refactoring approach**: Extract the value_1..N pattern into a loop. Extract common event processing into a shared method.

### All MQL4 Utility Functions Always Included

`add_global_functions()` includes ~50+ MQL4 functions in EVERY generated EA regardless of whether the strategy uses them. This bloats output.

**Refactoring approach**: Track which functions are referenced by the generated code and only include those. Or use `#include` files.

### Security Issues

- Hardcoded AES key in `encryption.py` (line 7) for encrypting error tracebacks
- CORS fully open (`allow_origins=["*"]` with `allow_credentials=True`)
- No request body validation (raw `request.json()`, no Pydantic models)

### Module-Level Path Evaluation

Multiple modules do `path = path_root.get()` at import time (line 5 of `block_constructor.py`, etc.). This creates stale references if `set_base_path()` were ever called later. Currently safe because `set_base_path()` is never called, but it's a latent bug.

### Other Backend Issues

- Debug `print("keys_lost: " + str(keys_lost))` left in `adapter.py` line 243
- `is_not_const_var()` is O(n) linear scan for every value check — no caching
- `/api/generate` and `/api/generate/preview` are identical endpoints — preview does nothing different
- `generation_service.py` imports `HTTPException` (web framework type) — violates separation of concerns
- `remove_repetitive_enums_custom_indicator()` uses `set()` which destroys ordering (non-deterministic output)
- Uses deprecated `@app.on_event("startup")` instead of modern FastAPI lifespan

---

## 8. Frontend Technical Debt

### No Undo/Redo

No history tracking. Every edit is permanent until page refresh.

### No Persistence/Autosave

Strategy state is entirely in memory. Page refresh = total loss. Need localStorage backup or server-side save.

### No Pre-Generation Validation

No checks for: empty required params, disconnected nodes, missing variable references, circular edges, type mismatches.

### GenericConfig Silently Drops Nested Params

`Object.entries(params).filter(([_, v]) => typeof v !== 'object')` hides any param that's an object. This works for condition nodes (which have their own config), but any OTHER block type with nested params would silently lose them in the UI.

### ProjectOptions Uses Python-Style String Booleans

`virtual_stops: 'True'` instead of `true`. This is because the original generator was Python-only and used Python's string representation. The frontend perpetuates this.

### Hardcoded Frontend Constants That Mirror Backend

These must be kept in sync manually:
- `CATEGORY_NODE_TYPE` (18 entries in BlockPalette)
- `CATEGORY_LABELS` (18 entries in BlockPalette)
- `CATEGORY_EVENT_RESTRICTION` (11 entries in BlockPalette)
- `INDICATORS` (31 entries in IndicatorSelector)
- `OPERATORS` (8 entries in ConditionConfig)
- `fieldOptions.ts` (70+ field name → dropdown options mappings)

**Refactoring approach**: Move this metadata to the backend API. Add a `GET /api/templates/metadata` endpoint that returns category → node type mapping, event restrictions, and field option definitions. The `fieldOptions.ts` data should ideally live in the backend near the `input.json` files, perhaps as an `options.json` companion file.

### Inconsistent Edge ID Generation

- `onConnect`: `id: \`e-${Date.now()}\``
- `duplicateNodes`/`pasteNodes`: `id: uid()`

### nextIdByUser Never Reset on Strategy Load

When loading a strategy (from AI or file), the `loadStrategy()` method replaces all event graphs but doesn't update `nextIdByUser` to be max(all id_by_user) + 1. This means new nodes added after loading could have conflicting `id_by_user` values.

---

## 9. The Dropdown/Enum Field System

### How It Works Now

- `fieldOptions.ts` maps field names to `{ value, label }[]` option arrays
- `getFieldOptions(fieldName, currentValue)` does the lookup with smart detection:
  - Direct lookup by field name in the static map
  - Color fields detected by name pattern (ending in `color`/`Color`)
  - Boolean fields detected by value (`true`/`false`)
  - `timeframe` field: numeric values → numeric options, `PERIOD_*` strings → string options
- `GenericConfig.tsx` calls `getFieldOptions()` for every param and passes options to `ParamInput`
- `ParamInput` renders `<select>` when options are provided, `<input>` otherwise
- `ensureCurrentValue()` appends the current value if it's not in the options list (safety net)

### Potential Issues

- If a new block is added with a field name that collides with an existing one in `fieldOptions.ts` but has different valid values, the wrong dropdown will appear
- The `mode` field is particularly risky — it's used by many indicators with DIFFERENT valid values (MACD: MODE_MAIN/MODE_SIGNAL vs Bollinger: MODE_MAIN/MODE_UPPER/MODE_LOWER vs Alligator: MODE_GATORJAW/TEETH/LIPS). Currently all modes are lumped into one list.
- Boolean auto-detection by value means a field that's coincidentally `"true"` as a string (not a boolean) would get a True/False dropdown

---

## 10. Contents Directory Structure

```
backend/contents/
├── block/                    # Block class template (block_template.json)
├── block_i/                  # Block instance template (class_template.json, initializer.json)
├── block_parent/             # Block parent class template
├── task/                     # Task base class template
├── task_id/                  # Task instance template
├── tasks/                    # Per-task-type templates (19 categories)
│   ├── buy_sell/
│   │   └── buy_sell/         # input.json + 5 code template JSONs
│   ├── condition_formula/
│   │   ├── condition_1_normal/
│   │   └── condition_1_cross/
│   ├── trading_actions/
│   │   ├── close_trades/
│   │   ├── delete_pending_orders/
│   │   └── modify_stops_of_trades/
│   ├── trailing_stop_break_even/
│   │   ├── trailing_stop_each_trade/
│   │   ├── break_even_point_each_trade/
│   │   └── trailing_pending_orders/
│   ├── loop_for_trades_orders/
│   │   ├── for_each_trade/
│   │   ├── for_each_pending_order/
│   │   ├── for_each_closed_trade/
│   │   ├── close_partially/
│   │   ├── check_profit/
│   │   ├── check_loss/
│   │   ├── check_type/
│   │   ├── check_age/
│   │   ├── modify_stops/
│   │   └── pips_away_from_open_price/
│   ├── check_trades_orders_count/
│   ├── check_trading_conditions/
│   ├── time_filters/
│   ├── various_signals/
│   ├── chart_objects/
│   ├── loop_for_chart_objects/
│   ├── controlling_blocks/
│   ├── output_communication/
│   ├── modify_variables/
│   └── various_actions/
├── indicators/               # Per-indicator templates (33 indicators)
│   ├── rsi/
│   ├── ma/
│   ├── macd/
│   └── ... (30 more)
├── candle/                   # Candle value fetch template
├── value/                    # Static value template
├── value_fetch/              # Nested value source templates
│   ├── market_properties/
│   ├── indicators-my-indicators/
│   └── ...
├── object_on_the_chart/      # Chart object property templates
└── miscellaneous/
```

Each task block directory contains:
- `input.json` — default parameter values (what the frontend shows as defaults)
- `field_data.json` — MQL4 class member field declarations
- `constructor_data.json` — MQL4 constructor body
- `run_data.json` — MQL4 run method body
- `reset_data.json` — MQL4 reset method body
- `function_data.json` — additional MQL4 methods

---

## 11. Priority Refactoring Targets

### High Priority (bugs / correctness)
1. **Variable reference `@` prefix handling** — Verify the serializer strips `@` before sending to backend, or add this translation
2. **nextIdByUser on strategy load** — Reset to max(id_by_user)+1 when loading
3. **Test fixtures** — Fix `conftest.py` to use correct field names matching `input.json`
4. **IndicatorSelector** — Load indicator-specific params dynamically from API instead of showing only 5 generic params

### Medium Priority (maintainability)
5. **Move hardcoded mappings to backend API** — CATEGORY_NODE_TYPE, CATEGORY_LABELS, CATEGORY_EVENT_RESTRICTION, INDICATORS list should come from the backend
6. **Selection coordination** — Extract the mutual-exclusion logic between editorStore.selectedNodeId and strategyStore.selectedVarConst into a single function/store
7. **Caching** — Cache template files and block metadata at backend startup
8. **Request validation** — Add Pydantic models to /api/generate

### Low Priority (long-term architecture)
9. **Replace string .replace() templating** — Use Jinja2 or delimited placeholders (`{{key}}`)
10. **Undo/redo** — Add history tracking to editorStore
11. **Persistence** — localStorage autosave + server-side strategy storage
12. **Pre-generation validation** — Check for disconnected nodes, missing params, type mismatches
13. **Tree-shake MQL4 utility functions** — Only include functions the strategy actually uses
14. **ExpertBuilder deduplication** — Extract the value_1..N loops and common event processing

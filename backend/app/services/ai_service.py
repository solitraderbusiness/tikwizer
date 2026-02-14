import json
import httpx
import uuid


SYSTEM_PROMPT = """You are an expert MQL4 trading strategy designer for the Tikwizer visual strategy builder.

Your job is to convert natural language strategy descriptions into a node graph JSON format.

Available block types (use these exact block_name_mql values):
- buy_now (category: buy_sell) - Place a market buy order
- sell_now (category: buy_sell) - Place a market sell order
- condition (category: condition_formula) - Compare two values (indicators, candles, numbers)
- once_per_bar (category: time_filters) - Only trigger once per bar
- time_filter (category: time_filters) - Filter by time of day
- spread_filter (category: time_filters) - Filter by spread size
- loop_for_trades (category: loop_for_trades_orders) - Loop through open trades
- close_trade_in_loop (category: trading_actions) - Close a trade (inside loop)
- trailing_stop (category: trailing_stop_break_even) - Apply trailing stop
- check_trades_count (category: check_trades_orders_count) - Check number of open trades
- and_gate (category: condition_formula) - AND logic gate
- or_gate (category: condition_formula) - OR logic gate
- pass (category: various_signals) - Pass-through node

For conditions, the params.operator.label can be: ">", "<", ">=", "<=", "==", "!=", "×>" (cross above), "×<" (cross below)
For condition left/right sides, use this structure:
{
  "row1": "indicator",  // or "value", "candle"
  "row2": "rsi",        // indicator name
  "params": { "period": "14", "applied_price": "PRICE_CLOSE", "shift": "0", ... }
}
For numeric values: { "row1": "value", "row2": "Numeric", "params": { "value": "70" } }

Return ONLY valid JSON in this exact format:
{
  "events": {
    "on_tick": {
      "nodes": [
        {
          "id": "<uuid>",
          "id_by_user": <integer>,
          "blockName": "<display name>",
          "block_name_mql": "<internal name>",
          "category": "<category>",
          "params": { ... },
          "enabled": true,
          "position": { "x": <number>, "y": <number> }
        }
      ],
      "edges": [
        {
          "id": "<uuid>",
          "source": "<source-node-id>",
          "sourceHandle": "blue",
          "target": "<target-node-id>",
          "targetHandle": "c"
        }
      ]
    },
    "on_init": { "nodes": [], "edges": [] },
    "on_timer": { "nodes": [], "edges": [] },
    "on_trade": { "nodes": [], "edges": [] },
    "on_chart": { "nodes": [], "edges": [] },
    "on_deinit": { "nodes": [], "edges": [] }
  },
  "variables": [],
  "constants": [],
  "project_options": {
    "magic_and_other": { "magic_number": "12345", "expiration_date": " ", "on_timer_period": "600" },
    "pip_size": { "rules": "0.001 = 0.015\\n0.016 = 0.0001\\n0.000001 = 0.0001\\n" },
    "description_and_version_number": { "copy_right": "", "description": "", "website_address": "", "version_number": "1.0" },
    "virtual_stops": { "virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100" },
    "visual": { "display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False" }
  }
}

Position nodes in a top-to-bottom flow with ~200px vertical spacing. Use sourceHandle "blue" for true/pass paths and "red" for false/fail paths.
Generate unique UUIDs for all ids."""


async def generate_strategy_from_prompt(prompt: str, api_key: str) -> dict:
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "anthropic/claude-sonnet-4",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.3,
            },
        )
        response.raise_for_status()
        data = response.json()

    content = data["choices"][0]["message"]["content"]

    # Extract JSON from the response (handle markdown code blocks)
    if "```json" in content:
        content = content.split("```json")[1].split("```")[0]
    elif "```" in content:
        content = content.split("```")[1].split("```")[0]

    strategy = json.loads(content.strip())

    # Ensure all nodes have required fields
    for event_key, event_data in strategy.get("events", {}).items():
        for node in event_data.get("nodes", []):
            if "id" not in node:
                node["id"] = str(uuid.uuid4())
            if "enabled" not in node:
                node["enabled"] = True

    return {"strategy": strategy}

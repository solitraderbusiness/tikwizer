# Tikwizer - MQL4 Visual Strategy Builder

## Project Overview
Tikwizer is a SaaS web app that wraps an existing Python MQL4 code generator (923 JSON templates) with a FastAPI backend and React Flow visual editor, letting traders visually create strategies and generate MetaTrader Expert Advisors (.mq4 files).

## Architecture
- **Backend:** FastAPI (Python 3.12) at `backend/` - wraps the existing generator
- **Frontend:** React + TypeScript + Vite + React Flow + Zustand + Tailwind CSS v4 at `frontend/`
- **Generator:** Original Python MQL4 generator at `backend/app/generator/` (moved from `pyfiles/`)
- **Templates:** 923 JSON templates at `backend/contents/` providing MQL4 code structures

## Running Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python3 -m app.main
# Runs on http://localhost:8001
```

### Frontend
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:5173
```

### Docker
```bash
docker compose up --build -d
# Frontend: http://localhost:3001
# Backend API: http://localhost:8002
```

### Environment Variables
- `OPENROUTER_API_KEY` - Required for AI strategy generation (see `.env.example`)

## Key Directories
- `backend/app/main.py` - FastAPI entry point
- `backend/app/api/` - API routes (generate, templates, ai)
- `backend/app/services/` - Business logic services
- `backend/app/generator/` - Core MQL4 generator (Python modules)
- `backend/contents/` - JSON templates for code generation (19 categories, 102 blocks)
- `backend/contents/tasks/` - Block templates organized by category subdirectories
- `backend/contents/indicators/` - Indicator templates
- `frontend/src/components/` - React components (layout, editor, nodes, config, context-menu, ai)
- `frontend/src/components/editor/context-menu/` - Right-click context menus (node, edge, canvas)
- `frontend/src/components/editor/config/` - Node parameter config panels + field option registry
- `frontend/src/components/editor/nodes/` - Custom node components including GroupNode
- `frontend/src/stores/` - Zustand state stores (editorStore, strategyStore)
- `frontend/src/lib/` - Utilities (serializer, uid)
- `frontend/src/api/` - API client

## API Endpoints
- `POST /api/generate` - Generate MQL4 from strategy JSON
- `POST /api/generate/preview` - Preview generation
- `GET /api/templates/blocks` - List available block types (dynamically scanned from `contents/tasks/`)
- `GET /api/templates/indicators` - List available indicators
- `POST /api/ai/generate-strategy` - AI-powered strategy generation

## Data Flow
1. User builds strategy visually on React Flow canvas
2. Frontend serializer converts React Flow nodes/edges to generator JSON format
3. Backend adapter.refactor() restructures and validates data
4. ExpertBuilder generates complete MQL4 code from templates
5. Generated .mq4 code returned and displayed/downloadable

## Block Palette
- Blocks are fetched dynamically from `/api/templates/blocks` (not hard-coded)
- Each block's `default_params` come from `input.json` in its template directory
- Categories are filtered by active event tab (e.g. "On Trade Events" only shows in `on_trade`)
- Event restriction mapping is in `BlockPalette.tsx` (`CATEGORY_EVENT_RESTRICTION`)
- Category-to-nodeType mapping is in `BlockPalette.tsx` (`CATEGORY_NODE_TYPE`)
- Search filters blocks by name and auto-expands matching categories

## Node Parameter Config
- `GenericConfig.tsx` is the default config panel — renders all flat params from `input.json`
- Specialized configs exist: `BuySellConfig.tsx`, `TimeFilterConfig.tsx`, `ConditionConfig.tsx`
- `ParamInput.tsx` is the universal field component — renders as text input OR dropdown select
- `fieldOptions.ts` is the registry mapping 70+ field names to their dropdown option lists
- Dropdown detection: `getFieldOptions(fieldName, currentValue)` checks the registry, color field name patterns, boolean values, and numeric/string timeframe variants
- All param fields support variable/constant references via `@varName` prefix and the `{x}` picker button
- Variable references are type-checked: numeric fields only show int/double vars, string fields show string vars

## Constants & Variables
- Managed in `strategyStore.ts` (not editorStore)
- Listed as clickable items at the top of the Block Palette sidebar
- Clicking one opens a property panel on the right (VariablesPanel) with type, name, value, description
- Property panel and node ConfigPanel are mutually exclusive
- Can be referenced in any node param field via `@variableName` syntax

## Context Menus & Keyboard Shortcuts
- Right-click nodes: Edit Title, Copy/Cut/Duplicate, Enable/Disable, Detach, Info, Create Area, Delete
- Right-click edges: Delete Connection
- Right-click canvas: Paste
- Keyboard: Del (delete), Ctrl+C/X/V/D (copy/cut/paste/duplicate), Escape (close menus)
- Clipboard operations stored in `editorStore.clipboard`

## Conventions
- Backend: Python with relative imports within `generator/` package
- Frontend: TypeScript strict mode, functional components, Zustand for state
- Styling: Tailwind CSS v4 + CSS custom properties (--color-*)
- Node types: conditionNode, actionNode, filterNode, loopNode, controlNode, groupNode
- Edge connections: "blue" = true/pass path, "red" = false/fail path
- Context menu components use React portals to `document.body`
- Nginx config uses Docker DNS resolver (`127.0.0.11`) for upstream resolution
- `tsc -b` (used by Docker) is stricter than `tsc --noEmit` — always verify with both

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

### Environment Variables
- `OPENROUTER_API_KEY` - Required for AI strategy generation (see `.env.example`)

## Key Directories
- `backend/app/main.py` - FastAPI entry point
- `backend/app/api/` - API routes (generate, templates, ai)
- `backend/app/services/` - Business logic services
- `backend/app/generator/` - Core MQL4 generator (Python modules)
- `backend/contents/` - JSON templates for code generation
- `frontend/src/components/` - React components (layout, editor, nodes, config, ai)
- `frontend/src/stores/` - Zustand state stores
- `frontend/src/lib/` - Utilities (serializer)
- `frontend/src/api/` - API client

## API Endpoints
- `POST /api/generate` - Generate MQL4 from strategy JSON
- `POST /api/generate/preview` - Preview generation
- `GET /api/templates/blocks` - List available block types
- `GET /api/templates/indicators` - List available indicators
- `POST /api/ai/generate-strategy` - AI-powered strategy generation

## Data Flow
1. User builds strategy visually on React Flow canvas
2. Frontend serializer converts React Flow nodes/edges to generator JSON format
3. Backend adapter.refactor() restructures and validates data
4. ExpertBuilder generates complete MQL4 code from templates
5. Generated .mq4 code returned and displayed/downloadable

## Conventions
- Backend: Python with relative imports within `generator/` package
- Frontend: TypeScript strict mode, functional components, Zustand for state
- Styling: Tailwind CSS v4 + CSS custom properties (--color-*)
- Node types: conditionNode, actionNode, filterNode, loopNode, controlNode
- Edge connections: "blue" = true/pass path, "red" = false/fail path

import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.generate import router as generate_router
from app.api.templates import router as templates_router
from app.api.ai import router as ai_router

app = FastAPI(title="Tikwizer API")

# ---------------------------------------------------------------------------
# CORS
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Route mounting
# ---------------------------------------------------------------------------
app.include_router(generate_router, prefix="/api")
app.include_router(templates_router, prefix="/api")
app.include_router(ai_router, prefix="/api")

# ---------------------------------------------------------------------------
# Startup event
# ---------------------------------------------------------------------------
CONTENTS_DIR = Path(__file__).resolve().parent.parent / "contents"


@app.on_event("startup")
async def startup_event() -> None:
    """Verify (and create if missing) the contents/ directory."""
    if not CONTENTS_DIR.exists():
        CONTENTS_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created missing contents directory: {CONTENTS_DIR}")
    else:
        print(f"Contents directory verified: {CONTENTS_DIR}")


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------
@app.get("/")
async def health_check():
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)

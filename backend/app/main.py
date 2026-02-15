import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.generate import router as generate_router
from app.api.templates import router as templates_router
from app.api.ai import router as ai_router

app = FastAPI(title="Tikwizer API")

# ---------------------------------------------------------------------------
# CORS
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Route mounting — API routes first
# ---------------------------------------------------------------------------
app.include_router(generate_router, prefix="/api")
app.include_router(templates_router, prefix="/api")
app.include_router(ai_router, prefix="/api")

# ---------------------------------------------------------------------------
# Startup event
# ---------------------------------------------------------------------------
CONTENTS_DIR = Path(__file__).resolve().parent.parent / "contents"
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"


@app.on_event("startup")
async def startup_event() -> None:
    if not CONTENTS_DIR.exists():
        CONTENTS_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created missing contents directory: {CONTENTS_DIR}")
    else:
        print(f"Contents directory verified: {CONTENTS_DIR}")

    if FRONTEND_DIR.exists():
        print(f"Frontend build found: {FRONTEND_DIR}")
    else:
        print(f"No frontend build at {FRONTEND_DIR} — API-only mode")


# ---------------------------------------------------------------------------
# Serve built frontend (SPA fallback)
# ---------------------------------------------------------------------------
if FRONTEND_DIR.exists():
    # Serve static assets (JS, CSS, images)
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIR / "assets")), name="static-assets")

    # SPA fallback: any non-API route serves index.html
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        file_path = FRONTEND_DIR / full_path
        if file_path.is_file():
            return FileResponse(str(file_path))
        return FileResponse(str(FRONTEND_DIR / "index.html"))
else:
    @app.get("/")
    async def health_check():
        return {"status": "ok"}


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)

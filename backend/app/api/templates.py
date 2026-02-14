import json
import os
from fastapi import APIRouter, HTTPException

router = APIRouter()

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENTS_DIR = os.path.join(BACKEND_DIR, "contents")
TASKS_DIR = os.path.join(CONTENTS_DIR, "tasks")
INDICATORS_DIR = os.path.join(CONTENTS_DIR, "indicators")


def _is_visible_directory(parent: str, name: str) -> bool:
    """Return True if the entry is a non-hidden directory."""
    if name.startswith("."):
        return False
    return os.path.isdir(os.path.join(parent, name))


def _make_display_name(name: str) -> str:
    """Convert a snake_case directory name into a Title Cased display name."""
    return name.replace("_", " ").title()


def _load_input_json(directory: str) -> dict:
    """Load input.json from a directory, returning an empty dict on failure."""
    path = os.path.join(directory, "input.json")
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


@router.get("/templates/blocks")
async def list_blocks():
    """Scan contents/tasks/ and return all block templates grouped by category."""
    if not os.path.isdir(TASKS_DIR):
        raise HTTPException(status_code=500, detail="Tasks directory not found")

    categories = []

    for category_name in sorted(os.listdir(TASKS_DIR)):
        if not _is_visible_directory(TASKS_DIR, category_name):
            continue

        category_path = os.path.join(TASKS_DIR, category_name)
        blocks = []

        for block_name in sorted(os.listdir(category_path)):
            if not _is_visible_directory(category_path, block_name):
                continue

            block_path = os.path.join(category_path, block_name)
            default_params = _load_input_json(block_path)

            blocks.append({
                "name": block_name,
                "display_name": _make_display_name(block_name),
                "category": category_name,
                "default_params": default_params,
            })

        categories.append({
            "category": category_name,
            "blocks": blocks,
        })

    return categories


@router.get("/templates/indicators")
async def list_indicators():
    """Scan contents/indicators/ and return all indicator templates."""
    if not os.path.isdir(INDICATORS_DIR):
        raise HTTPException(status_code=500, detail="Indicators directory not found")

    indicators = []

    for indicator_name in sorted(os.listdir(INDICATORS_DIR)):
        if not _is_visible_directory(INDICATORS_DIR, indicator_name):
            continue

        indicator_path = os.path.join(INDICATORS_DIR, indicator_name)
        default_params = _load_input_json(indicator_path)

        indicators.append({
            "name": indicator_name,
            "display_name": _make_display_name(indicator_name),
            "default_params": default_params,
        })

    return indicators

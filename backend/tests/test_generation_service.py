import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.generation_service import generate
from fastapi import HTTPException


def test_generate_wraps_data_key(minimal_strategy):
    """If input already has 'data' key, it should work."""
    result = generate(minimal_strategy)
    assert "code" in result
    assert "filename" in result
    assert result["filename"] == "expert_output.mq4"


def test_generate_auto_wraps_missing_data_key():
    """If input does NOT have 'data' key, service wraps it."""
    inner = {
        "events": {
            "on_init": {"nodes": [], "edges": []},
            "on_timer": {"nodes": [], "edges": []},
            "on_tick": {"nodes": [], "edges": []},
            "on_trade": {"nodes": [], "edges": []},
            "on_chart": {"nodes": [], "edges": []},
            "on_deinit": {"nodes": [], "edges": []},
        },
        "variables": [],
        "constants": [],
        "project_options": {
            "magic_and_other": {"magic_number": "55225", "expiration_date": " ", "on_timer_period": "600"},
            "pip_size": {"rules": "0.001 = 0.015\n"},
            "description_and_version_number": {"copy_right": "", "description": "", "website_address": "", "version_number": "1.0"},
            "virtual_stops": {"virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100"},
            "visual": {"display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False"},
        },
    }
    result = generate(inner)
    assert "code" in result


def test_generate_bad_data_raises_http_exception():
    with pytest.raises(HTTPException) as exc_info:
        generate({"garbage": True})
    assert exc_info.value.status_code == 500

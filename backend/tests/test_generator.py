"""Basic smoke test for the restructured generator."""
import sys
import os

# Add backend to path so `app.generator` resolves
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.generator import mql_generator


# Minimal test input — a simple buy_now node
TEST_DATA = {
    "data": {
        "events": {
            "on_init": {"nodes": [], "edges": []},
            "on_timer": {"nodes": [], "edges": []},
            "on_tick": {
                "nodes": [
                    {
                        "params": {
                            "slippage": "4",
                            "comment": "",
                            "lot_size": "0.01",
                            "money_management": "fixed_lot",
                            "stop_loss": "0",
                            "take_profit": "0",
                            "group": "",
                        },
                        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                        "id_by_user": 1,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now",
                        "enabled": True,
                    }
                ],
                "edges": [],
            },
            "on_trade": {"nodes": [], "edges": []},
            "on_chart": {"nodes": [], "edges": []},
            "on_deinit": {"nodes": [], "edges": []},
        },
        "variables": [],
        "constants": [],
        "project_options": {
            "magic_and_other": {
                "magic_number": "55225",
                "expiration_date": " ",
                "on_timer_period": "600",
            },
            "pip_size": {
                "rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n"
            },
            "description_and_version_number": {
                "copy_right": "Test",
                "description": "Test EA",
                "website_address": "",
                "version_number": "1.0",
            },
            "virtual_stops": {
                "virtual_stops": "True",
                "virtual_stops_time_out": 0,
                "emergency_stops": "always",
                "relative_size": 0,
                "add_pips": "100",
            },
            "visual": {
                "display_spread_meter": "True",
                "display_status_messages": "False",
                "display_indicators_after_test": "False",
            },
        },
    }
}


def test_basic_generation():
    result = mql_generator.generate_mql(TEST_DATA)
    assert isinstance(result, str), "Result should be a string"
    assert not result.startswith("ERROR:"), f"Generator returned error: {result[:200]}"
    assert "OnTick" in result, "Generated code should contain OnTick handler"
    assert "OnInit" in result, "Generated code should contain OnInit handler"
    print(f"SUCCESS: Generated {len(result)} chars of MQL4 code")
    print("First 200 chars:")
    print(result[:200])


if __name__ == "__main__":
    test_basic_generation()

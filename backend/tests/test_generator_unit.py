import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.generator import mql_generator, adapter, path_root


def test_path_root_returns_backend_dir():
    path = path_root.get()
    assert path.endswith("backend") or "backend" in path
    assert os.path.isdir(path)


def test_path_root_contents_dir_exists():
    path = path_root.get()
    contents_dir = os.path.join(path, "contents")
    assert os.path.isdir(contents_dir)


def test_path_root_set_base_path():
    original = path_root.get()
    path_root.set_base_path("/tmp/test")
    assert path_root.get() == "/tmp/test"
    # Reset
    path_root.set_base_path(None)
    path_root._base_path = None
    assert path_root.get() == original


def test_adapter_refactor_sets_enabled():
    """adapter.refactor should set enabled=True on nodes missing it."""
    data = {
        "data": {
            "events": {
                "on_init": {"nodes": [], "edges": []},
                "on_timer": {"nodes": [], "edges": []},
                "on_tick": {
                    "nodes": [
                        {
                            "params": {"slippage": "4", "comment": "", "group": ""},
                            "id": "test-node-1",
                            "id_by_user": 1,
                            "blockName": "Buy now",
                            "category": "buy_sell",
                            "block_name_mql": "buy_now",
                            # No 'enabled' key
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
                "magic_and_other": {"magic_number": "55225", "expiration_date": " ", "on_timer_period": "600"},
                "pip_size": {"rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n"},
                "description_and_version_number": {"copy_right": "", "description": "", "website_address": "", "version_number": "1.0"},
                "virtual_stops": {"virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100"},
                "visual": {"display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False"},
            },
        }
    }
    result = adapter.refactor(data)
    node = result["events"]["on_tick"]["nodes"][0]
    assert node["enabled"] is True


def test_generate_mql_returns_string():
    data = {
        "data": {
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
                "pip_size": {"rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n"},
                "description_and_version_number": {"copy_right": "", "description": "", "website_address": "", "version_number": "1.0"},
                "virtual_stops": {"virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100"},
                "visual": {"display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False"},
            },
        }
    }
    result = mql_generator.generate_mql(data)
    assert isinstance(result, str)


def test_generate_mql_error_returns_error_string():
    """Passing garbage data should return ERROR: prefix."""
    result = mql_generator.generate_mql({"data": {"events": {}, "variables": [], "constants": []}})
    assert isinstance(result, str)
    assert result.startswith("ERROR:")

import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def minimal_strategy():
    """Minimal valid strategy with a single buy_now node."""
    return {
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


@pytest.fixture
def condition_with_buy_strategy():
    """Strategy with a condition node connected to a buy node via blue edge."""
    return {
        "data": {
            "events": {
                "on_init": {"nodes": [], "edges": []},
                "on_timer": {"nodes": [], "edges": []},
                "on_tick": {
                    "nodes": [
                        {
                            "params": {
                                "operator": {"label": ">"},
                                "left": {
                                    "row1": "indicator",
                                    "row2": "rsi",
                                    "params": {
                                        "period": "14",
                                        "applied_price": "PRICE_CLOSE",
                                        "shift": "0",
                                    },
                                },
                                "right": {
                                    "row1": "value",
                                    "row2": "Numeric",
                                    "params": {"value": "70"},
                                },
                            },
                            "id": "cond-1111-2222-3333-444444444444",
                            "id_by_user": 1,
                            "blockName": "Condition",
                            "category": "condition_formula",
                            "block_name_mql": "condition",
                            "enabled": True,
                        },
                        {
                            "params": {
                                "slippage": "4",
                                "comment": "",
                                "lot_size": "0.1",
                                "money_management": "fixed_lot",
                                "stop_loss": "50",
                                "take_profit": "100",
                                "group": "",
                            },
                            "id": "buy-5555-6666-7777-888888888888",
                            "id_by_user": 2,
                            "blockName": "Buy now",
                            "category": "buy_sell",
                            "block_name_mql": "buy_now",
                            "enabled": True,
                        },
                    ],
                    "edges": [
                        {
                            "source": "cond-1111-2222-3333-444444444444",
                            "sourceHandle": "blue",
                            "target": "buy-5555-6666-7777-888888888888",
                            "targetHandle": "c",
                            "type": "customEdge",
                            "id": "edge-1",
                        }
                    ],
                },
                "on_trade": {"nodes": [], "edges": []},
                "on_chart": {"nodes": [], "edges": []},
                "on_deinit": {"nodes": [], "edges": []},
            },
            "variables": [],
            "constants": [{"id": "const-1", "type": "double", "name": "x", "value": "1.5", "description": "test"}],
            "project_options": {
                "magic_and_other": {"magic_number": "12345", "expiration_date": " ", "on_timer_period": "600"},
                "pip_size": {"rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n"},
                "description_and_version_number": {"copy_right": "Test", "description": "RSI Strategy", "website_address": "", "version_number": "1.0"},
                "virtual_stops": {"virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100"},
                "visual": {"display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False"},
            },
        }
    }


@pytest.fixture
def empty_strategy():
    """Strategy with no nodes at all."""
    return {
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
                "magic_and_other": {"magic_number": "99999", "expiration_date": " ", "on_timer_period": "600"},
                "pip_size": {"rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n"},
                "description_and_version_number": {"copy_right": "", "description": "", "website_address": "", "version_number": "1.0"},
                "virtual_stops": {"virtual_stops": "True", "virtual_stops_time_out": 0, "emergency_stops": "always", "relative_size": 0, "add_pips": "100"},
                "visual": {"display_spread_meter": "True", "display_status_messages": "False", "display_indicators_after_test": "False"},
            },
        }
    }

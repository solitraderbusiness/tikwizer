import task_constructor
import global_functions
import constants_constructor
import global_vars
import indicator_class_constructor
import candle_class_constructor
import value_class_constructor
import market_properties_class_constructor


value = {
        "row1": {
            "label": "Indicator"
        },
        "row2": {
            "name": "RSI",
            "description": "this is RSI indicator"
        },
        "params": [
            {
                "optionName": "symbol",
                "value": {
                    "value": 14
                }
            },
            {
                "optionName": "timeframe",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            },
            {
                "optionName": "period",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            },
            {
                "optionName": "applied_price",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            },
            {
                "optionName": "buy_threshold",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            },
            {
                "optionName": "sell_threshold",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            },
            {
                "optionName": "shift",
                "value": {
                    "value": "PRICE_CLOSE"
                }
            }
        ]
}


class value_data:
    properties = ""
    consts_system = ""
    consts_user = ""
    vars_system = ""
    vars_user = ""
    structs = ""
    classes = ""
    functions = ""
    initializer = ""
    var_name = ""

data = value_data()



def parse_value(value):
    row1 = value.get("row1")
    match row1:
        case "Indicator":
            return parse_indicator(value)
        case "Market Properties":
            return parse_market_properties(value)
        case "Candle":
            return parse_candle(value)
        case "Value":
            return parse_value(value)


def parse_indicator (value, suffix):
    name = value.get("row2").get("name")
    mclass = indicator_class_constructor.get_class(name, value.get("input_dic"), suffix)
    initializer = indicator_class_constructor.get_initializer(name, suffix)
    var_name =  indicator_class_constructor.get_var_name(name, suffix)

    data.classes = mclass
    data.initializer = initializer
    data.var_name = var_name
    return data

def parse_market_properties (value, suffix):
    mclass = market_properties_class_constructor.get_class(value.get("input_dic"), suffix)
    initializer = market_properties_class_constructor.get_initializer(suffix)
    var_name = market_properties_class_constructor.get_var_name(suffix)
    structs = market_properties_class_constructor.get_structs()

    data.classes = mclass
    data.initializer = initializer
    data.var_name = var_name
    data.structs = structs
    return data

def parse_candle (value, suffix):
    mclass = candle_class_constructor.get_class(value.get("input_dic"), suffix)
    initializer = candle_class_constructor.get_initializer(suffix)
    var_name = candle_class_constructor.get_var_name(suffix)

    data.classes = mclass
    data.initializer = initializer
    data.var_name = var_name
    return data

def parse_value (value, suffix):
    mclass = value_class_constructor.get_class(value.get("input_dic"), suffix)
    initializer = value_class_constructor.get_initializer(suffix)
    var_name = value_class_constructor.get_var_name(suffix)

    data.classes = mclass
    data.initializer = initializer
    data.var_name = var_name
    return data



























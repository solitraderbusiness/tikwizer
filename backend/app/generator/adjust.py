# pips returns sth like this: a + toDigits(20, NULL)
# % returns sth like this: a * 20/NormalizeDouble(100,0)
# % returns sth like this: a + a * 20/NormalizeDouble(100,0)
# last returns sth like this: a + 20
def get(mstr, value, symbol):
    value = value.strip()
    if value == "":
        return mstr
    elif value.endswith("pips"):
        if value.startswith("+"):
            return mstr + " + " + "toDigits( " + value[1:len(value) - 4] + "," + symbol + ")"
        elif value.startswith("-"):
            return mstr + " - " + "toDigits( " + value[1:len(value) - 4] + "," + symbol + ")"
        elif value.startswith("*"):
            return mstr + " * " + "toDigits( " + value[1:len(value) - 4] + "," + symbol + ")"
        elif value.startswith("/"):
            return mstr + " / " + "toDigits( " + value[1:len(value) - 4] + "," + symbol + ")"
        else:  # Supposing it has no prefix which means default is used: +
            return mstr + " + " + "toDigits( " + value[0:len(value) - 4] + "," + symbol + ")"
    elif value.endswith("%"):  # postfix is %
        if value.startswith("+"):
            return mstr + " + " + mstr + "*" + value[1:len(value) - 1] + "/NormalizeDouble(100,0)"
        elif value.startswith("-"):
            return mstr + " - " + mstr + "*" + value[1:len(value) - 1] + "/NormalizeDouble(100,0)"
        elif value.startswith("*"):
            return mstr + "*" + value[1:len(value) - 1] + "/NormalizeDouble(100,0)"
        elif value.startswith("/"):
            return mstr + " / " + value[1:len(value) - 1] + "/NormalizeDouble(100,0)"
        else:  # Supposedly it has no prefix which means +
            return mstr + " + " + mstr + "*" + value[0:len(value) - 1] + "/NormalizeDouble(100,0)"
    else:  # Empty postfix
        if value.startswith("+"):
            return mstr + " + " + value[1:len(value) + 1]
        elif value.startswith("-"):
            return mstr + " - " + value[1:len(value) + 1]
        elif value.startswith("*"):
            return mstr + " * " + value[1:len(value) + 1]
        elif value.startswith("/"):
            return mstr + " / " + value[1:len(value) + 1]
        else:  # Supposing it has no prefix which means default is used: +
            return mstr + " + " + value[0:len(value) + 1]

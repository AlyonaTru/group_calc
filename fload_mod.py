# inner function of number conversion
def make_float(tofloat: str) -> float:
    neg = False
    if tofloat[0] == '-':
        neg = True
        tofloat = tofloat[1:]
    try:
        tofloat = float(tofloat)
    except ValueError:
        return -1
    if neg:
        return -tofloat
    else:
        return tofloat


# inner function of string processing
def parse_str(args):
    opers = []
    opers.append(make_float(args[0]))
    opers.append(args[1])
    opers.append(make_float(args[2]))
    return opers


# inner function of operation handling
def make_operation(x: float, sign: str, y: float, ) -> float:
    match sign:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


# external call function
def process_float(args) -> str:
    res_str = str(round(make_operation(*parse_str(args)), 2))
    return res_str


print(process_float(['-0.333', '+', '44.22']))  # - call example

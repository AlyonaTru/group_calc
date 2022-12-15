from re import split, search


# внутренняя функция перевода в число
def make_float(tofloat: str) -> float:
    try:
        return float(tofloat)
    except ValueError:
        return -1


# внутренняя функция обработки строки
def parse_str(toparse: str):
    opers = list(map(make_float, split('[-+*/]', toparse)))
    sign = toparse[search('[-+*]', toparse).start()]
    return *opers, sign


# внутрення функция обработки операции
def make_operation(x: float, y: float, sign: str) -> float:
    match sign:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


# функция внешнего вызова
def processing(expr_str: str) -> str:
    res_str = str(round(make_operation(*parse_str(expr_str)), 2))
    return res_str

# print(processing('0.333+44.22')) - пример вызова

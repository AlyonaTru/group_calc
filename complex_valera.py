from re import search


# ну такая слабенькая проверка выражения
def is_expression_ok(expression) -> bool:
    if expression.count('j') != 2:
        return False
    if {'-', '+', '*', '/'}.isdisjoint(expression):
        return False
    try:
        for i in range(expression.count('j')):
            if expression[expression.index('j') - 2] not in {'-', '+'}:
                return False
    except:
        return False
    return True


# создать комплексное число из строки. предполагается, что строка имеет вид +\-a+\-bj
def make_complex(num: str) -> complex:
    neg1 = False  # отрицательная ли вещественная часть
    if num[0] == '-':
        neg1 = True
        num = num[1:]
    j = num.index('j') + 1  # индекс буквы в мнимной части
    sign_idx = search('[-+*/]', num).start()  # поиск операции
    first_num = float(num[:sign_idx]) if not neg1 else -float(num[:sign_idx])  # число вещ. части со знаком
    sec_num = float(num[sign_idx + 1:j - 1]) if num[sign_idx] == '+' else -float(num[sign_idx + 1:j - 1])  # и мнимой
    oper = complex(first_num, sec_num)  # преобразование в комплексное число
    return oper


def parse_c_str(expression: str):
    expression = expression.replace(' ', '')
    firstj = expression.index('j')
    oper1 = make_complex(expression[:firstj + 1])
    sign = expression[firstj + 1:firstj + 2]
    oper2 = make_complex(expression[firstj + 2:])
    return oper1, oper2, sign


def make_operation(x: complex, y: complex, sign: str) -> str:
    res = ''
    match sign:
        case '+':
            res = str(x + y)
        case '-':
            res = str(x - y)
        case '*':
            res = str(x * y)
        case '/':
            res = str(x / y)
    return res.replace('(', '').replace(')', '')


#print(make_operation(*parse_c_str('-4+3j - 3+4j')))  # debug
# 4*(5+1)-(9+2/4)+2*(40-5+6-7)
from math import sqrt
import re

exit_sign = ''
line_str = ''
brake_line_str = ''
match_str = ''
line_lst = []
sign_lst = []
brake_lst = []
match_lst = []
SIGN_TYPE = ['*', '/', '+', '-']
switch_counter = 0


def line_input():
    global line_str, brake_line_str
    check = True
    while check:
        try:
            line_str = (input('Для выхода введите Q. Введите выражение: '))
            check = False
        except ValueError:
            print('\033[31mНеверный ввод!\033[0m')
    brake_line_str = line_str
    sign_input()


def sign_input():
    global sign_lst, line_lst, SIGN_TYPE
    sign_lst = list(filter(lambda x: x in SIGN_TYPE, line_str))
    operands_lst = list(re.split('[-+*/]', line_str))
    line_lst = [x for y in zip(operands_lst, sign_lst) for x in y]
    line_lst.append(operands_lst[-1])
    print(f'\033[032mLine input: {line_lst}\033[0m')
    switch()
    return line_str


def switch():
    global switch_counter, line_lst
    if 'Q' in ''.join(line_str):
        exit()
    elif 'j' in ''.join(line_str):
        switch_counter = 1
        for i in range(len(sign_lst)):
            operations_priority()
    elif '%' in ''.join(line_str):
        switch_counter = 2
        send_operands(switch_counter)
    elif re.match(r'sqrt', line_str):
        switch_counter = 3
        send_operands(switch_counter)
    elif '(' in line_str:
        switch_counter = 4
        brake_sign_list_create()
        brake_ops_list_create()
    elif re.findall('[0-9.]', line_str):
        switch_counter = 5
        for i in range(len(sign_lst)):
            operations_priority()
    else:
        print('\033[31mНеверный ввод!\033[0m')
        line_input()


def send_operands(pared_operands):
    global switch_counter
    match switch_counter:
        case 1:
            return complex_calc(pared_operands)
        case 2:
            print(percent_calc(line_str))
        case 3:
            print(sqrt_calc(line_str))
        case 4:
            return ratio_calc(pared_operands)


def complex_calc(operands):
    operand1, sign, operand2 = operands
    operand1 = complex(operand1)
    operand2 = complex(operand2)
    if sign == '*':
        return operand1 * operand2
    if sign == '/':
        return operand1 / operand2
    if sign == '+':
        return operand1 + operand2
    if sign == '-':
        return operand1 - operand2


def percent_calc(ops_str):
    operand1, operand2 = ops_str.split('%')
    percent = float(operand1) * 100 / float(operand2)
    return percent


def sqrt_calc(ops_str):
    operand = float(ops_str[4:])
    sq_routine = sqrt(operand)
    return round(sq_routine, 2)


def ratio_calc(operands):
    operand1, sign, operand2 = operands
    operand1 = float(operand1)
    operand2 = float(operand2)
    if sign == '*':
        return round(operand1 * operand2, 2)
    if sign == '/':
        return round(operand1 / operand2, 2)
    if sign == '+':
        return round(operand1 + operand2, 2)
    if sign == '-':
        return round(operand1 - operand2, 2)


def brake_sign_list_create():
    global sign_lst, line_str
    ds_lst = list(re.split('\(.*?\)', line_str))
    ds_str = ''.join(ds_lst)
    sign_lst = list(re.findall('[-+*/]', ds_str))


def brake_ops_list_create():
    global brake_lst
    pattern = re.compile(r'\([\d+*/-]+\)')
    pos = 0
    while True:
        match = pattern.search(line_str, pos)
        if not match:
            break
        s = match.start()
        e = match.end()
        brake_lst.append(line_str[s:e])
        pos = e
    if '(' in brake_line_str:
        brake_operations()
    else:
        sign_input()


def brake_operations():
    global line_str, sign_lst, brake_lst, match_lst, match_str
    line_str = brake_lst[0][1:-1]
    match_str = line_str
    match_lst = ['(' + line_str + ')']
    while re.findall(r'[+*/-]+', ''.join(sign_lst)):
        sign_input()


def replace_operands(operands):
    global line_lst, sign_lst, switch_counter
    switch_counter = 4
    operand1, sign, operand2 = operands
    line_lst.pop(line_lst.index(sign) - 1)
    line_lst.insert(line_lst.index(sign), send_operands(operands))
    line_lst.pop(line_lst.index(sign) + 1)
    line_lst.pop(line_lst.index(sign))
    sign_lst.pop(sign_lst.index(sign))
    print(f'\033[033mResult: {line_lst}\033[0m')
    if not re.findall(r'[+*/-]+', ''.join(sign_lst)):
        brake_replace_operands()


def brake_replace_operands():
    global brake_line_str, line_lst, brake_lst, match_lst
    try:
        brake_lst.remove(*match_lst)
    except:
        line_input()
    brake_line_str = brake_line_str.replace(('(' + match_str + ')'), str(*line_lst))
    line_lst.clear()
    sign_lst.clear()
    brake_ops_list_create()
    sign_input()


def curr_operation(sign):
    global line_lst
    op_index = line_lst.index(sign)
    pared_operands = [line_lst[op_index - 1], line_lst[op_index], line_lst[op_index + 1]]
    replace_operands(pared_operands)
    return pared_operands


def operations_priority():
    while len(sign_lst) > 0:
        for sign in sign_lst:
            if sign == '*':
                return curr_operation(sign)
            elif sign == '/':
                return curr_operation(sign)
        for sign in sign_lst:
            if sign == '+':
                return curr_operation(sign)
            elif sign == '-':
                return curr_operation(sign)


while True:
    line_input()

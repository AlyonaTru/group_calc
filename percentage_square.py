import math
from operator import pow, truediv, mul, add, sub


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}


def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

calc = input("Ввод _ 1:\n")
print("Ответ: " + str(calculate(calc)))

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
    "^": lambda x, y: math.pow(x, y),
    "%": lambda x, y: str(100 * float(x)/float(y))
}


def calculate(expr):
    numxChars = ""
    operation = None
    numyChars = ""
    for char in expr:
        if char.isdigit():
            if operation is None:
                numxChars += char
            else:
                numyChars += char
        elif char in operations:
            operation = char
        elif char.isspace:
            pass
        else:
            raise Exception("Ошибочка: " + char)
    return operations[operation](int(numxChars), int(numyChars))

print(calculate(input("Ввод _ 2_ : ")))


def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return str(percentage) + "%"

print("VIVOD, к примеру 3,5 : Вывод _ 3 _ : " + percentage(3,5))



def percent(expression):
    if "%" in expression:
        expression = expression.replace("%","/100")
    return eval(expression)


print(percent(input("Ввод _ 4 _ : ")))


def square(nums):
    print("Исходный список целых чисел:")
    print(nums)
    print("\nКвадратное каждое число в указанном списке:")
    square_nums = list(map(lambda x: x ** 2, nums))
    print(square_nums)
    print("\nКуб каждое число указанного списка:")
    cube_nums = list(map(lambda x: x ** 3, nums))
    print(cube_nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square(nums)

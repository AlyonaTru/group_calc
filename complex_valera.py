lst=[1+2j, 2+4j]

def complex_sum(lst):
    a=lst[0]
    b=lst[1]
    #a = 1 + 2j 
    #b = 2 + 4j 
    rez = lst[0]+lst[1]
    #print('Addition =', a + b)
    #print('Subtraction =', a - b)
    #print('Multiplication =', a * b)
    #print('Division =', a / b)
    print(rez)
complex_sum(lst)

def complex_sub(lst):
    rez=lst[0]-lst[1]
    print(rez)
    return rez
complex_sub(lst)

def complex_mult(lst):
    rez = lst[0]*lst[1]
    print(rez)
complex_mult(lst)

def complex_div(lst):
    rez = lst[0]/lst[1]
    print(rez)
complex_div(lst)
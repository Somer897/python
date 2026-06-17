import math

def func(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        return math.sin(a) / math.cos(b) + c**0.5
    except ValueError:
        print('Не численное значение!!!')
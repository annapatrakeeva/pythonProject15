import math

PI = math.pi


def radius():
    n = float(input('Диаметр цилиндра:'))
    n /= 2
    return n


def height():
    m = float(input('Высота цилиндра:'))
    return m


def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s * h
    return v

#print('Объем цилиндра', volume(), 'см3')
def massa(g):
    n = float(input('плотность:'))
    return g*n/1000
print('Вес цилиндра в кг', massa(volume()))


"""
3. Описати функцію Mediana(A, B, C) дійсного типу, яка знаходить медіану трикутника.
"""


import math


def check(a_0, b_0, c_0):
    if a_0 or b_0 or c_0 < 0:
        return f'Невірно вказано значення'
    else:
        return median_(a_0, b_0, c_0)


def median_(a, b, c):
    return 0.5 * math.sqrt(2 * math.pow(a, 2) + 2 * math.pow(b, 2) - math.pow(c, 2)), \
           0.5 * math.sqrt(2 * math.pow(a, 2) + 2 * math.pow(c, 2) - math.pow(b, 2)), \
           0.5 * math.sqrt(2 * math.pow(c, 2) + 2 * math.pow(b, 2) - math.pow(a, 2))


ab = float(input('AB = '))
bc = float(input('BC = '))
ac = float(input('AC = '))
print(check(ab, bc, ac))
input()
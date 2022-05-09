"""
Розділ 4.
1. Описати функцію Power1 (A, B) дійсного типу, яка знаходить величину AB за формулою
AB = exp (B ln (A)) (параметри A і B - дійсні).
У разі нульового або негативного параметра A функція повертає 0.
З допомогою цієї функції знайти
степені AP, BP, CP, якщо дано числа P, A, B, C.
"""


import math


def power1(a, b):
    if b > 0:
        return math.exp(b * math.log1p(a))
    else:
        return 0


p_ = float(input('P = '))
a_ = float(input('A = '))
b_ = float(input('B = '))
c_ = float(input('C = '))
print(power1(p_, a_))
print(power1(p_, b_))
print(power1(p_, c_))
input()
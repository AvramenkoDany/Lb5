"""
Розділ 3.
1. Описати функцію IsPrime (N) логічного типу, яка повертає True, якщо цілий
параметр N (> 1) є простим числом, і False в іншому випадку (число, більше 1,
називається простим, якщо воно не має позитивних дільників, крім 1 і самого себе).
Дано набір з 10 цілих чисел, більших 1. За допомогою функції IsPrime знайти
кількість простих чисел в даному наборі.
"""


import math
import random


def isprime(n):
    if n - 1 <= 0:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def input_():
    n = 1
    while n <= 10:
        print(f'Enter the value {n}: ')
        output_(random.randint(0, 1000))
        n += 1


def output_(val):
    print('Value = ', val, "and It's natural?  ", isprime(val))


input_()
input()

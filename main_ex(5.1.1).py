"""
Розділ 1.
1. Описати функцію PowerA3 (A, B), яка обчислює третю ступінь числа A і повертає її в
змінну B (A - вхідний, B - вихідний параметр; обидва параметри є дійсними). За
допомогою цієї функції знайти треті ступені п'яти даних чисел.
"""


import math


def main(a):
    b = math.pow(a, 3)
    return f'result: {b}'


def input_():
    n = 1
    while n <= 5:
        output = float(input(f'Enter the value {n}: '))
        output_(output)
        n += 1


def output_(val):
    print(main(val))


input_()
input()
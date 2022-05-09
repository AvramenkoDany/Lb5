"""
Розділ 2.
1. Описати функцію Sign (X) цілого типу, яка повертає для дійсного числа X наступні
значення: -1, якщо X <0; 0, якщо X = 0; 1, якщо X> 0. За допомогою цієї функції
знайти значення виразу Sign (A) + Sign (B) для даних дійсних чисел A і
B.
"""


def main(x: float):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
    

def calc(a, b):
    return main(a) + main(b)


a_ = float(input('Enter X1: '))
b_ = float(input('Enter X2: '))
result = calc(a_, b_)
print(result)


#
# створити функцію генератор простих (освіжіть собі у памяті що таке прості числа !!!!)
# чисел у дипазоні заданих двома аргументами чисел.
# Вивести у консоль результат роботи функції-генератора в діапазоні
# від N до Z в один рядок через прогалину. N і Z - числа діапазону які можна вибирати випадковим чином.

import random


def is_prime(n):
    '''Функція яка вираховує чи число є простим'''
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func(n, z):
    '''Функція, що генерує прості числа в діапазоні заданому від N до Z'''
    for i in range(n, z + 1):
        if is_prime(i):
            yield i


n = random.randint(2, 10)
print('n = ', n)

z = random.randint(10, 33)
print('z = ', z)

for k in func(n, z):
    print(k, end = ' ')
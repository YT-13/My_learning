# #1
# Напишіть програму, яка виводить квадратну матрицю розміру N на N. У кожному непарному рядку матриці йдуть числа від -N до -1,
# а в кожному парному — просто числа, що дорівнюють номеру цього рядка.
#
# N = запросити у користувача
#
# Вивести результат у вигляді матриці чисел.
#
# +2 бала до роботи якщо будете використовувати форматуваня так щоб числа які мають більше
# цифр не спотворювали візуальне представлення матриці.

n = int(input("Ведіть число від 5 до 10 >>> "))
import random
k = [[x for x in range(1,n + 1)] if l % 2 ==0 else [random.randint(-n, -1) for x in range(1, n+1)] for l in range(1, n+ 1)]
for i in range(0,len(k)):
    print(f'{k[i]}')
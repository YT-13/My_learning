#2
# Напишіть програму, яка виводить квадратну матрицю розміру N на N заповнену випадковими числами.
# N = запросити у користувача
# Вивести значення у вигляді матриці чисел.
# Вивести в термінал - суму чисел по діагоналі
# Вивесті на єкран суму чисел остнанього стовбця. (Можна використити вираз і функцію sum())

# matrix = int(input("Ведіть число від 5 до 10"))
matrix = int(input("Enter your number >>> "))
import random

k = [[random.randint(0, matrix) for n in range(0, matrix + 1)] for j in range(0, matrix +1)]
for i in range(0,len(k)):
    print(f'{k[i]}')

n = 0
suma = 0
m = 0
for i in range(0, len(k)):
    m += k[i][-1]
    suma += k[i][n]
    n+=1

print(f'сума чисел по діагоналі матриці = {suma}')
print(f'сума чисел останнього стовбця матриці = {m}')
# Напишіть програму, Яка генерує список із 15 випадкових чисел.
# Виведіть:
# Так - якщо сумма непарних чисел у списку більша за суму парних чисел
# Ні - у всіх інших випадках

import random
lst = [random.randint(0, 15) for x in range(0, 15)]
if sum(lst) % 2 == 0:
    print('Yes')
else:
    print('No')
# A. (47 балів)Створити файл у якому реалізувати способи обміну значень 2х змінних. Домовимось
# що значення змінних мають бути будь-які цілі числа:
#
# заміна значень 2х змінних використовючи 3-тю змінну - рузультат вивести на/в термінал
# заміна значень 2х змінних використовуючи властивості python - рузультат вивести на/в термінал
# (завдання з зірочкою +3 бали до завдання) заміна значень 2 змінних не використівуючи 2х попредніх варіантів.

# метод 1
a = 33
b = 44
c = a
a = b
b = c
print(a, b)

# метод 2:
a = 33
b = 44
a, b = b, a
print(a, b)

#метод 3:
a = 33
b = 44
a = a + b
b = a - b
a = a - b
print(a, b)

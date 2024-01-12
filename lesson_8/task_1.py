# Завдання 1
# Створити список чисел в діапазоні 10, 250, необхідно видалити всі входження чисел, які
#  діляться без остачі на  20, із нього. Вивести результуючий список в термінал.

# my_list = []
# for i in range(20, 251):
#     my_list.append(i)
#     if i % 20 ==0:
#         my_list.remove(i)
# print(my_list)

# my_list = []
# for i in range(20, 251):
#     if i % 20 !=0:
#         my_list.append(i)
# print(my_list)

my_list1 = list(range(20, 251))
for i in my_list1:
    if i % 20 == 0:
        my_list1.remove(i)
print(my_list1)
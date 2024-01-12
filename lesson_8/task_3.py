# Є 2 списки:
# [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
# [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
# Порахувати скільки разів числа з одного списку зустрічаються у ішому списку. Вивести у вигляді відформатованої таблиці.

first_list = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
second_list = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]

for i in first_list:
    print(f'{i:^3} -  {second_list.count(i)}')

print('\n')

for x in second_list:
    print(f'{x:^3} - {first_list.count(x)}')
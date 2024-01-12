# Программа запитує ввід з клавіатури цілі числа по черзі - до того часу поки не буде введено 0.
# Як тільки буде введено 0 программа повинна порахувати і вивести в термінал
#
# Сумму чисел
# Середнє арифметичне усіх введених чисел (не враховуючи останнього 0)
# Визначити максимальне і мінімальне занчення
# Визначити кількість парних та кількість не парних чисел

serednya = 0
len_str = ''
parni = 0
neparni = 0
max_number = int()
min_number = int()
while True:
    a = int(input('enter your number'))
    if a == 0:
        break
    else:
        max_number = a
        min_number = a
        if a < min_number:
            min_number = a
        if a > max_number:
            max_number = 0
        else:
            pass
        len_str += str(a)
        serednya += a

        if a % 2 == 0:
            len_parni += str(a)
        else:
            len_neparni += str(a)

print("Сума всіх чисел = ", serednya)
print("Середнє арифметичне всіх чисел = ", serednya / len(len_str))
print('максиммальне число = ', max_number, 'Мінімальне число = ', min_number)
print('Кількість парних хначень = ',len(len_parni), "Кількість непарних значень = ", len(len_neparni))
# input_list=[]
# while True:
#     number = int(input('enter your number >>> '))
#     if number == 0:
#         break
#     input_list.append(number)
#
# print('Ви ввели числа: ', input_list)
#
# print('Сума введених чисел: ', sum(input_list))
# print('Максимальне введене число: ', max(input_list))
# print('Мінімальне введене число: ',min(input_list))
#
# n = 0
# k = 0
# for i in range(len(input_list)):
#     if input_list[i] % 2 == 0:
#         n +=1
#     else:
#         k +=1
# print('Кількість введених парних чисел: ', n,)
# print('Кількість введених непарних чисел: ', k)
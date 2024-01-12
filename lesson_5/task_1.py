# Вввести натуральне число і впевнитись що в ньому є 2 однакові цифри(не обовязково такі що стоять разом)
# Наприклад:
#
# input
# number:
# 123452
# Так
#
# input
# number:
# 123456
# Ні


number = input("Введіть будь яке число (мінімум трьохзначне) >>> ")
if len(number) < 3:
    print('Число має бути мінімум трьохзначне')
else:
    count = 0
    for i in range(len(number)):
       for j in range(i+1, len(number)):
           if number[i] == number[j]:
                count+=1
    if count >= 1:
        print('Так')
    else:
        print('Ні')
# Створіть словник із випадковими числовими значеннями довжиною в 20 елементів.
# Необхідно їх (числові значення) перемножити і вивести на екран згенерований на початку словник та результат множення чисел.

#перші спроби:
# import random
# list_1 = [random.randint(0, 20) for i in range(0, 20)]
# print(list_1)
# list_2 = [ x*x for x in list_1]
# print((list_2))
# dict_1 = dict(zip(list_1, list_2))
# print(dict_1)

our_dict = { i : i*i for i in range(1, 21)}
print(our_dict)

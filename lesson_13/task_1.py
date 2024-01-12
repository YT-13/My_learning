# Створити декоруєму функцію яка повертає множину чисел.
# - аргументом функціі приймається ціле число що харектиризує кількість елементів у множині повино бути.
# Створити функцию декоратор.
# Декоратор повинен вивести числа у вигляді таблиці (чи добре відформатованому вигляді) у відсортированому порядку.
# Де до кожного числа повинен бути коментар - чи число кратне 3 чи ні і чи парне число чи ні
def first_decoration(func):

    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        numb = 3
        para = 'парне'
        nepara = 'не парне'
        kratne = 'кратне'
        nekratne = 'не кратне'
        for i in return_value:
            if i % 3 == 0:
                if i % 2 == 0:
                    print(f'{i:>2} {kratne:^10} {numb} {para:<8}')
                else:
                    print(f'{i:>2} {kratne:^10} {numb} {nepara:<8}')
            else:
                if i % 2 == 0:
                    print(f'{i:>2} {nekratne:^10} {numb} {para:<8}')
                else:
                    print(f'{i:>2} {nekratne:^10} {numb} {nepara:<8}')
    return wrapper

@first_decoration
def number_set(number : int):
    our_set = {i + (i+1) for i in range(0, number)}
    print(our_set)
    return our_set

@first_decoration
def second_number_set(number = 8):
    my_set = {i + 3 for i in range(0, number)}
    print(my_set)
    return my_set

number_set(3)

second_number_set(8)



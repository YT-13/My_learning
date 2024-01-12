# Напишіть функцію яка приймає 3 параметри - словник, ключ та значення за замовчуванням.
#
# dict_handler(link_on_dict: dict, key, default_value)
# За допомогою try/exept/finaly - отримайте значеня по ключу - якщо такого ключа не має -
# створити в словникові пару де ключем виступатиме key (аргумент 2 - функціі),
# а значенням default_value (аргумент 3 -  функції).
# Увага - якщо key змінюваний тип данних то він не може бути ключем словника.
# У такому випадку - сгенеруйте виключну ситуацію з певним поясненням що трапилось.
#
# Функція повертає те що в результаті зберігається в словнику за ключем key.



def dict_handler(dict, key='y', default_value=13):

    try:
        return dict[key]

    except TypeError:
        print('key змінюваний тип данних, він не може бути ключем словника')


    except KeyError:
        dict[key] = default_value
        print(f'Даного ключа не має в списку, тож dict[key] = значенню по замовчуванню {dict[key]}')
        return dict[key]


our_dict = {"a": 4, "m": 9}
result = dict_handler(our_dict, ["a"])
print(result)


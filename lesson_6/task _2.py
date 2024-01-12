# 2.
# Користувач вводить окремо рядок (string) і один символ (char).
# Необхідно здійснити пошук у рядку `string` всіх символів `char`.
#
# Для вирішення потрібно використовувати тільки функцію `find()`(rfind()),
# оператори `if` і `for`(while)

# string = input("Введіть ваш рядок з символом(ми)")
index = ''
string = '123@345@'
# chair = input("Введіть ваш символ")
chair = '@'

for i in string:
    index = string.find(chair)
    last_index = string.rfind(chair)
print('В даному рядку символ знаходиться у таких індексах рядка - ', index, last_index)



while True:
    index = string.find(chair)
    last_index = string.rfind(chair)
    print('В даному рядку символ знаходиться у таких індексах рядка -', index, last_index)
    break
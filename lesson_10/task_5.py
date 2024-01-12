# Створіть словник з рядка 'python is good language to code' наступним чином: як ключі візьміть літери рядка,
# а значеннями нехай будуть числа, що відповідають кількості входження даної літери в рядок.

our_string = 'python is good language to code'

first_list = [i for i in our_string if i != ' ']

second_list = [first_list.count(x) for x in first_list]

result_dict = dict(zip(first_list, second_list))

print(result_dict)
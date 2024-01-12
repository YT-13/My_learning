
def buble_sort(list_to_sort_1: list) -> list:

    """ сортуємо список методом бульбашки, у циклі перебераємо елементи і
    найменший елемент пересуваємо ліворуч списку"""

    n = len(list_to_sort_1)
    for i in range(n):
        for x in range(n-2, i-1, -1):
            if list_to_sort_1[x] > list_to_sort_1[x+1]:
                list_to_sort_1[x],  list_to_sort_1[x + 1] = list_to_sort_1[x+1], list_to_sort_1[x]
    return list_to_sort_1


def rock_sort(list_to_sort: list) -> list:

    """ сортуємо список методом камінцем, у циклі перебераємо елементи і
    найбільший елемент пересуваємо ліворуч списку"""

    n = len(list_to_sort)
    for i in range(0, n-1):
        for x in range(0,n-1):
            if list_to_sort[x] < list_to_sort[x+1]:
                list_to_sort[x+1], list_to_sort[x] = list_to_sort[x], list_to_sort[x+1]
    return list_to_sort


def my_sort(list_to_sort: list) -> list:

    '''кожного разу в циклі шукаємо найменший елемент,
    добавляємо його в новий список і видаляємо із старого,
    також від довжини старого списку віднімаємо одиницб
    :rtype: object'''

    new_list = []
    len_list = len(list_to_sort)
    while len_list !=0:
        for i in range(0, len_list):
            new_list.append(min(list_to_sort))
            list_to_sort.remove(min(list_to_sort))
            len_list -= 1
    return new_list


_all_ = ['buble_sort', 'rock_sort', 'my_sort']

if __name__ == "__main__":

    to_sort = [3, 5, 22, 8, 2, 4, 11, 9]
    to_sort_1 = [1, 23, 22, 7, 2, 32, 15, 13]

    print(rock_sort(to_sort))
    print(buble_sort(to_sort_1))
    print(my_sort([3,5,2,6,3,33,2,1]))
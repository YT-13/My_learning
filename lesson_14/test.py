def buble_sort(list_to_sort: list) -> list:
    """ """
    n = len(list_to_sort)
    for i in range(n):
        for x in range(n-2, i-1, -1):
            if list_to_sort[x] > list_to_sort[x+1]:
                list_to_sort[x],  list_to_sort[x + 1] = list_to_sort[x+1], list_to_sort[x]
                print(to_sort)
    return list_to_sort

def rock_sort(list_to_sort: list) -> list:
    n = len(list_to_sort)
    for i in range(0, n-1):
        for x in range(0,n-1):
            if list_to_sort[x] < list_to_sort[x+1]:
                list_to_sort[x+1], list_to_sort[x] = list_to_sort[x], list_to_sort[x+1]
                print(to_sort)
    return list_to_sort


if __name__ == "__main__":
    to_sort = [3, 5, 22, 8, 2, 4, 11, 9]
    # print(buble_sort(to_sort))
    print(rock_sort(to_sort))

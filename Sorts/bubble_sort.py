def is_sorted(items_list):
    for i in range(len(items_list) - 1):
        if items_list[i] > items_list[i + 1]:
            return False
    return True


def bubble_sort(items_list):
    while not is_sorted(items_list):
        for i in range(len(items_list) - 1):
            if items_list[i] > items_list[i + 1]:
                temp = items_list[i]
                items_list[i] = items_list[i + 1]
                items_list[i + 1] = temp
    return items_list


my_list = [4, 2, 6, 5, 1, 3]
my_list = bubble_sort(my_list)
print(my_list)

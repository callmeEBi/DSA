def bubble_sort(items_list):
    for i in range(len(items_list) - 1, 0, -1):
        for j in range(i):
            if items_list[j] > items_list[j + 1]:
                items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]
    return items_list


my_list = [4, 2, 6, 5, 1, 3]
bubble_sort(my_list)
print(my_list)

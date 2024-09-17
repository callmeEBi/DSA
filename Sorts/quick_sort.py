def quick_sort(items_list):
    pivot = items_list[0]
    swap = 0
    i = 1
    while i < len(items_list):
        if items_list[i] < pivot:
            swap += 1
            items_list[swap], items_list[i] = items_list[i], items_list[swap]
        i += 1
    items_list[0], items_list[swap] = items_list[swap], items_list[0]
    return items_list


my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))

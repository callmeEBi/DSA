def insertion_sort(items_list):
    for i in range(1, len(items_list)):
        for j in range(i):
            if items_list[i] < items_list[j]:
                items_list[i], items_list[j] = items_list[j], items_list[i]
    return items_list


print(insertion_sort([4, 2, 6, 5, 1, 3]))

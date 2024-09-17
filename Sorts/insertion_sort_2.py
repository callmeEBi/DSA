def insertion_sort(items_list):
    for i in range(1, len(items_list)):
        temp = items_list[i]
        j = i - 1
        while j >= 0 and temp < items_list[j]:
            items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]
            j -= 1
    return items_list


print(insertion_sort([4, 2, 6, 5, 1, 3]))

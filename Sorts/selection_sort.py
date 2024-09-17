def selection_sort(items_list):
    for i in range(len(items_list)):
        min_index = i
        for j in range(i + 1, len(items_list)):
            if items_list[j] < items_list[min_index]:
                min_index = j
        items_list[i], items_list[min_index] = items_list[min_index], items_list[i]
    return items_list


my_list = [4, 2, 6, 5, 1, 3]
print(selection_sort(my_list))
# TODO - change the color of cursor (customize if possible)

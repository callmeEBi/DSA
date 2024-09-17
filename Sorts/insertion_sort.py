def insertion_sort(items_list):
    for i in range(1, len(items_list)):
        for j in range(i):
            if items_list[i] < items_list[j]:
                items_list[i], items_list[j] = items_list[j], items_list[i]

my_list = [4, 2, 6, 5, 1, 3]
insertion_sort(my_list)
print(my_list)

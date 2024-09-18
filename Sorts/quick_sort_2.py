def swapper(items_list, index1, index2):
    items_list[index1], items_list[index2] = items_list[index2], items_list[index1]


def pivot(items_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if items_list[i] < items_list[pivot_index]:
            swap_index += 1
            swapper(items_list, swap_index, i)
    swapper(items_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(items_list, left, right):
    if left < right:
        pivot_index = pivot(items_list, left, right)
        quick_sort_helper(items_list, left, pivot_index - 1)
        quick_sort_helper(items_list, pivot_index + 1, right)
    return items_list


def quick_sort(items_list):
    quick_sort_helper(items_list, left=0, right=len(items_list) - 1)


my_list = [4, 6, 1, 7, 3, 2, 5]
quick_sort(my_list)
print(my_list)

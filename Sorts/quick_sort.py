def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    test = quick_sort(less) + [pivot] + quick_sort(greater)
    return test


my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))

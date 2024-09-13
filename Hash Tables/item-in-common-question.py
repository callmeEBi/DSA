# we have two lists and we are looking for most efficient way to find out
# whether they have items in common with each other or not.

list1 = [1, 10, 9]
list2 = [99, 8, 10]


# first approach:
# this is o(n ^ 2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
        return False


# second approach
# this is o(n) which makes a huge difference in time complexity
def item_in_common(list1, list2):
    temp = {}
    for i in list1:
        temp[i] = None
    for j in list2:
        if j in temp:
            return True
    return False


print(item_in_common(list1, list2))

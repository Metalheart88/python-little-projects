# Implementation of binary search algorithm

# We will prove that binary search is faster than naive search

# naive search: scan the entire list and ask if it's equal to the target
# if yes, return the index
# if no, then return -1


def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer
# we will leverage the fact that our list is sorted
def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1
    midpoint = (low + high) // 2

    if high < low:
        return -1

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

#!/usr/local/bin/python3

# return the number of sets that add to total
# arr is sorted
def count_sets(arr, total):
    return rec(arr, total, arr.length-1)

# return the number of sets that add to total
# arr[i] could be add to sets of not, it's like recursive tree,
# left subtree add arr[i] to sets, right subtree don't
def rec(arr, total, i):
    if total == 0:
        return 1; # find a set that add to total
    if total < 0:
        return 0; # overflow set
    if i < 0:
        return 0;
    if total < arr[i]:
        return rec(arr, total, i-1) # way too big for total
    # main part of this func
    return rec(arr, total-arr[i], i-1) + \
            rec(arr, total, i-1)

if __name__ == "__main__":
    arr = array(2, 3, 4, 10)
    total = 15
    print(count_sets(arr, total))

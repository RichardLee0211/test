from https://leetcode.com/problems/two-sum/
solution1:
using Hash and numbertoFind = target - nunmbers[i]
well see other solutions
from youtube CS Dojo, Find sets of Numbers that add up to 16
```python
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

```
well, the problem of this recursive tree solution is that some subtrees are
exactly the same, waste time to calculate them again.
TODO: Dynamic programming??
solution1: memory solution
solution2:
```python
# return the number of sets that add to total
# arr is sorted
def count_sets(arr, total):
    mem = {} // empty dict or hash table
    return rec(arr, total, arr.length-1, mem)

# return the number of sets that add to total
# arr[i] could be add to sets of not, it's like recursive tree,
# left subtree add arr[i] to sets, right subtree don't
def rec(arr, total, i, mem):
    if key in mem:
        return mem[key]
    if total == 0:
        return 1; # find a set that add to total
    if total < 0:
        return 0; # overflow set
    if i < 0:
        return 0;
    if total < arr[i]:
        to_return = rec(arr, total, i-1) # way too big for total
    else:
        to_return=rec(arr, total-arr[i], i-1) + rec(arr, total, i-1)
    mem[key] = to_return
    return to_return
```

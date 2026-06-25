arr = [4, 7, 9, 10]
k = 1

def func(arr, k):
    

print(func(arr, k))

"""
BF:
- every time we come across a number that is <= to the target, we add one since it cannot possibly be the missing number

OPTIMAL:
- binary search to find the current diff between the number that should be there and the number that is actually there
- using the difference
    - if the diff is <= k, it means that the number is there are less missing numbers than needed
        - we'll check right to increase the number of missing numbers possible
- once the left and right cross, the answer is between the right and left pointers
- it would be right + (number needed (k) - number of missing numbers on the left)
"""

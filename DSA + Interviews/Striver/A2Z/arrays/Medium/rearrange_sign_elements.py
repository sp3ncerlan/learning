"""
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Example 1:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

Example 2:
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 
Positive elements = 1,2,3
Negative elements = -3,-1,-2
To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
Also, -3 should come before -1, and -1 should come before -2.

BRUTE FORCE:
- keep relative order
- collect all positives in to an array and all negatives into an array
- merge the two alternating
- O(n), O(n)

OPTIMAL:
- traverse the array once, keep an index for pos and neg placement and each time check if num is negative or positive and insert + increment
- O(n), O(n)
"""

# def rearrange(arr, k) -> int:
#     pos_arr, neg_arr = [], []
    
#     for num in arr:
#         if num > 0:
#             pos_arr.append(num)
#         else:
#             neg_arr.append(num)
            
#     result = [0] * k
#     for i in range(len(pos_arr)):
#         result[2 * i] = pos_arr[i]
#         result[2 * i + 1] = neg_arr[i]
    
#     return result

def rearrange(arr, k) -> int:
    pos_index, neg_index = 0, 1
    result = [0] * len(arr)
    
    for i in range(len(arr)):
        if arr[i] < 0:
            result[neg_index] = arr[i]
            neg_index += 2
        else:
            result[pos_index] = arr[i]
            pos_index += 2
    
    return result

arr = [1, 2, -3, -1, -2, 3]
k = len(arr)

print(rearrange(arr, k))

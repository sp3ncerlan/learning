"""
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Output:
  
Second Smallest : 2  
Second Largest : 5  
Explanation:
  The elements are sorted as 1, 2, 4, 5, 7, 7.  
Hence, the second smallest element is 2, and the second largest element is 5.

Example 2:
Input:
 [1]  
Output:
  
Second Smallest : -1  
Second Largest : -1  
Explanation:
  Since there is only one element in the array, it is both the largest and smallest element.  
Therefore, there is no second smallest or second largest element present.

Only one element can be the initial base case check
"""

def second_smallest_and_largest(arr) -> int:
    if len(arr) <= 1:
        return [-1, -1]
    
    smallest, largest = float('inf'), float('-inf')
    for num in arr:
        smallest = min(smallest, num)
        largest = max(largest, num)

    second_smallest, second_largest = float('inf'), float('-inf')
    for num in arr:
        if num < second_smallest and num != smallest:
            second_smallest = num
        
        if num > second_largest and num != largest:
            second_largest = num
    
    return [second_smallest, second_largest]

arr1 = [1, 2, 4, 7, 7, 5] # 2, 5
arr2 = [1] # -1, -1

print(second_smallest_and_largest(arr1))
print(second_smallest_and_largest(arr2))

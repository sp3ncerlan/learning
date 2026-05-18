"""
Problem Statement: Given an array, we have to find the largest element in the array.

Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5

Explanation:
5 is the largest element in the array.

Example 2:
Input:

 arr[] = {8, 10, 5, 7, 9}  
Output:
 10

Explanation:
10 is the largest element in the array.
"""

# def largest_element(arr) -> int: O(nlogn) for sorting
#     arr.sort(reverse=True)
#     return arr[0]

def largest_element(arr) -> int:
    largest = arr[0]
    
    for num in arr[1:]:
        largest = max(largest, num)
        
    return largest

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]

print(largest_element(arr1))
print(largest_element(arr2))


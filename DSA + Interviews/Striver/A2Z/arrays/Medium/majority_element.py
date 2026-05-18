"""
Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Example 1:
Input:
 nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
Output:
 7  
Explanation:
 The number 7 appears 5 times in the 9-sized array, making it the most frequent element.

Example 2:
Input:
 nums = [1, 1, 1, 2, 1, 2]  
Output:
 1  
Explanation:
 The number 1 appears 4 times in the 6-sized array, making it the most frequent element.
 
 BRUTE FORCE:
 - For each number in the array, go through the entire array and sum up its freq, then check if its > than floor division (total value count // 2)
 - O(n^2), O(1)
 
 BETTER:
 - Hashmap counting freq, check if > than floor division (total value count // 2)
 - O(n), O(n)
 
 OPTIMAL:
 - Count and Element fields, Boyer-Moore Voting algorithm
"""

def majority_element(arr) -> int:
    count, el = 0, 0
    
    for num in arr:
        if count == 0:
            el = num
            count = 1
        elif el == num:
            count += 1
        else:
            count -= 1
    
    # after getting the potential num, check if its actually > half
    final_count = arr.count(el)
    if final_count > (len(arr) // 2):
        return el

    return -1

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7] 

print(majority_element(arr))

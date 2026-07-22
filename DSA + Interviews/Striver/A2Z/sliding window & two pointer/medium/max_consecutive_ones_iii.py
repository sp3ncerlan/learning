nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 3

def func(nums, k):
    max_length = 0
    zero_count = 0
    
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
            
        if zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        # calc
        print(nums[left:right + 1])
        max_length = max(max_length, right - left + 1)
        
    return max_length

print(func(nums, k))

"""
Better approach:
- sliding window with zero counter

optimal:
- when we hit certain size, we move left + 1 as well no matter what and it will only expand if we find a larger window

Problem Statement: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
Output : 10
Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).
The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].
The number of consecutive 1's is 10.


Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3
Output : 9
Explanation : The underlines 1's are obtained by flipping 0's in the new array.
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].
The number of consecutive 1's is 9.
"""

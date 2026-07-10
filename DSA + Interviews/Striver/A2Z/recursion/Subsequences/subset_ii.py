nums = [1]

def recurse(nums, result, path, start):
    result.append(path[:])
    
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        
        path.append(nums[i])
        recurse(nums, result, path, i + 1)
        path.pop()
    
def func(nums):
    nums.sort()
    
    result = []
    path = []
    
    recurse(nums, result, path, 0)
    
    return result

print(func(nums))

"""
Problem Statement: Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.

Input: array[] = [1,2,2]
Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

Input: array[] = [1]
Output: [ [ ], [1] ]
Explanation: Only two unique subsets are available.
"""

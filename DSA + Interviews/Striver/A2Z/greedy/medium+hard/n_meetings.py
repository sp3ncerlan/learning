"""
Problem Statement: You are given a 0-indexed array nums of length n representing your maximum jump capability from each index.

You start at index 0. Each element nums[i] represents the maximum number of steps you can jump forward from index i.
Your goal is to reach the last index of the array (nums[n - 1]) using the minimum number of jumps
Return the minimum number of jumps required to reach the last index.
You can assume that it is always possible to reach the last index.

Input: nums = [2, 3, 1, 1, 4]

Output: 2
Explanation: Jump from index 0 → 1 → 4.

Input:
 nums = [2, 3, 0, 1, 4]

Output:
 2
Explanation:
 Jump from index 0 → 1 → 4.
"""
N = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]

def func(N, start, end):
    meetings = [(end[i], start[i], i + 1) for i in range(N)]
    meetings.sort(key=lambda x: x[0])
    prev_end = -1
    ans = []

    for end_time, start_time, i in meetings:
        if prev_end <= start_time:
            ans.append(i)
            prev_end = end_time

    return ans

print(func(N, start, end))
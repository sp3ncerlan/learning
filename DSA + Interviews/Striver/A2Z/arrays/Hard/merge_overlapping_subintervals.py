"""
Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input : intervals=[[1,3],[2,6],[8,10],[15,18]]
Output : [[1,6],[8,10],[15,18]]
Explanation : Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals.

Input : [[1,4],[4,5]]
Output :  [[1,5]]
Explanation :  Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].

BF:
- sort and then check each end with the next start to see if it overlaps
- take the min and max and make it one interval if overlap
- if not, then just add to new array
"""

intervals = [[1,4],[4,5]]

def func(intervals):
    result = []
    
    intervals.sort()
    
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        
        if len(result) == 0 or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)
            
    return result
        
print(func(intervals))

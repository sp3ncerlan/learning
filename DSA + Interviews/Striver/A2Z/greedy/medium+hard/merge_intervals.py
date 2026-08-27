"""
Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input : intervals=[[1,3],[2,6],[8,10],[15,18]]
Output : [[1,6],[8,10],[15,18]]
Explanation : Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals.

Input : [[1,4],[4,5]]
Output :  [[1,5]]
Explanation :  Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].
"""
intervals = [[1, 4], [4, 5]]

def func(intervals):
    intervals.sort()
    ans = []

    for i in range(len(intervals)):
        start, end = intervals[i]
        if ans and ans[-1][1] >= start:
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append(intervals[i])

    return ans

print(func(intervals))

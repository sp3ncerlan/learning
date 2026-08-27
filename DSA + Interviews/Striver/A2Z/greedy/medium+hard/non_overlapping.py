"""
Problem Statement: Given an array of N intervals in the form of (start[i], end[i]), where start[i] is the starting point of the interval and end[i] is the ending point of the interval, return the minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.
"""
intervals = [ [1, 3], [1, 4], [3, 5], [3, 4], [4, 5] ]

def func(intervals):
    intervals.sort(key=lambda x: x[1])
    meetings = []
    ans = 0

    for i in range(len(intervals)):
        start, end = intervals[i]

        if meetings and meetings[-1][1] > start:
            ans += 1
        else:
            meetings.append(intervals[i])

    return ans

print(func(intervals))

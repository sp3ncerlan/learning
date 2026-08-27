"""
Problem Statement: A line of N kids is standing there. The rating values listed in the integer array ratings are assigned to each kid. These kids are receiving candy according to the following criteria:

There must be at least one candy for every child.
Kids whose scores are higher than their neighbours receive more candies than their neighbours.
Return the minimum number of candies needed to distribute among children.

OPTIMAL:
- create an array of the same size as ratings
- iterate through it, and for each index, check the left and see if the current rating is greater. if it is, then we want to increase the amount of candies to candy[i - 1] + 1
"""
ratings = [1, 0, 5]

def func(ratings):
    n = len(ratings)
    candies = n

    i = 1
    while i < n:
        if ratings[i] == ratings[i - 1]:
            i += 1
            continue

        peak = 0
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            candies += peak
            i += 1

        valley = 0
        while i < n and ratings[i] < ratings[i - 1]:
            valley += 1
            candies += valley
            i += 1

        candies -= min(peak, valley)

    return candies

print(func(ratings))

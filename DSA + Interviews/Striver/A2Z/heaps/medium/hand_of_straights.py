import heapq
from collections import Counter, deque

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

def func(hand, group_size):
    freq = Counter(hand)
    min_heap = [key for key in freq.keys()]
    heapq.heapify(min_heap)

    while min_heap:
        first = min_heap[0]

        if freq[first] == 0:
            heapq.heappop(min_heap)
            continue

        for i in range(groupSize):
            card = first + i
            if freq[card] == 0:
                return False

            freq[card] -= 1

    return True

print(func(hand, groupSize))

"""
Problem Statement: You are given an array of integers hand, where hand[i] is the value on the i-th card that Alice owns. Alice wants to split her entire hand into groups such that: every group contains exactly groupSize cards, and the card values in each group form a sequence of groupSize consecutive integers (e.g. [3, 4, 5], [10, 11, 12, 13]).

Input : hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output :  True
Explanation :  One possible partition is [1,2,3] [2,3,4] [6,7,8].


Input : hand = [1,2,3,4,5], groupSize = 4
Output :  false
Explanation :  There is no way to split the hand into groups of 4 consecutive cards.
"""

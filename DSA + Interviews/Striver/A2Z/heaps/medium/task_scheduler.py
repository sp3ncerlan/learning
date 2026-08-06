import heapq
from collections import Counter, deque

tasks = ["A","A","A","B","B","B"]
n = 2

def func(tasks, n):
    counts = [0] * 26
    for t in tasks:
        counts[ord(t) - ord('A')] += 1

    max_heap = [-c for c in counts if c > 0]
    heapq.heapify(max_heap)

    queue = deque()
    time = 0
    while queue or max_heap:
        if not max_heap:
            time = queue[0][0]
        else:
            time += 1

        while queue and queue[0][0] <= time:
            # can push onto max_heap
            heapq.heappush(max_heap, queue.popleft()[1])

        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count < 0:
                queue.append((time + n + 1, count))

    return time

print(func(tasks, n))

"""
Problem Statement: You are given a list of tasks represented by uppercase English letters ('A' to 'Z'), and an integer n representing a cooldown interval between two same tasks. Each task takes exactly 1 CPU interval to complete. Tasks can be executed in any order, but identical tasks must be separated by at least n intervals, during which the CPU may remain idle or execute other tasks.
Return the minimum number of CPU intervals required to complete all the tasks.

Input :  tasks = ["A","A","A","B","B","B"], n = 2
Output :  8
Explanation : One valid execution order is:
A -> B -> idle -> A -> B -> idle -> A -> B
Total intervals = 8


Input :  tasks = ["A","C","A","B","D","B"], n = 1
Output : 6
 Explanation A possible execution:
A -> B -> C -> D -> A -> B
No idle interval is needed as cooldown = 1.
"""

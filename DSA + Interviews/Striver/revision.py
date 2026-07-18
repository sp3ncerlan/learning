from itertools import permutations
from collections import defaultdict
import math
import bisect

stack = []
# N = 3
# M = 2
# E = 3
# edges = [
#   (0, 1),  
#   (1, 2),
#   (0, 2)
# ]

def func(N, M, E, edges):
    adj = {u: [] for u in range(N)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * N
    
    def recurse(node):
        if node == N:
            return True
        
        for c in range(1, M + 1):
            is_safe = True
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    is_safe = False
                    break
                
            if is_safe:
                color[node] = c
                
                if recurse(node + 1):
                    return True
    
                color[node] = 0
                
        return False
    
    return 1 if recurse(0) else 0

print(func(N, M, E, edges))

"""
OPTIMAL:
- 
"""

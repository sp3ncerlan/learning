from collections import defaultdict

N = 4
M = 3
E = 5

edges = {
  (0, 1),  
  (1, 2),  
  (2, 3),  
  (3, 0),  
  (0, 2)  
}
    
def func(N, edges, M):
    # M = # of colors, N = # of nodes, E = # of edges
    adj = {i: [] for i in range(N)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * N
        
    def solve(node):
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
                
                if solve(node + 1):
                    return True
                
                color[node] = 0
            
        return False
    
    return 1 if solve(0) else 0

print(func(N, edges, M))

"""
Problem Statement: Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

Example 1:
Input:

N = 4  
M = 3  
E = 5  
Edges[] = {  
  (0, 1),  
  (1, 2),  
  (2, 3),  
  (3, 0),  
  (0, 2)  
}  
Output:
 1  
Explanation:
  
It is possible to color the given graph using 3 colors, so the answer is 1 (possible).

Example 2:
Input:
  
N = 3  
M = 2  
E = 3  
Edges[] = {  
  (0, 1),  
  (1, 2),  
  (0, 2)  
}  
Output:
 0  
Explanation:
  
It is not possible to color the graph using 2 colors as it forms a triangle, which requires at least 3 colors. Hence, the answer is 0 (not possible).
"""

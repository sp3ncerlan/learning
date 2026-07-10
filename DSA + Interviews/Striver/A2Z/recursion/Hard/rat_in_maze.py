n = 4
grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
    
def helper(n, grid, visited, result, path, row, col):
    if (row < 0 or row >= len(grid) or
        col < 0 or col >= len(grid[0]) or
        (row, col) in visited or
        grid[row][col] == 0):
        return
    
    if row == col == (n - 1):
        result.append(path)
        return
    
    visited.add((row, col))
    directions = [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]
    for dr, dc, mode in directions:
        nr, nc = row + dr, col + dc
        
        helper(n, grid, visited, result, path + mode, nr, nc)
    
    visited.remove((row, col))
   
def func(n, grid):
    result = []
    
    helper(n, grid, set(), result, "", 0, 0)
    
    return result

print(func(n, grid))

"""
Problem Statement: Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1). Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

Input: n = 4 , grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
Output: ["DDRDRR" , "DRDDRR"]
Explanation: The rat has two different path to reach (3, 3).
The first path is (0, 0) => (1, 0) => (2, 0) => (2, 1) => (3, 1) => (3, 2) => (3, 3).
The second path is (0,0) => (1,0) => (1,1) => (2,1) => (3,1) => (3,2) => (3,3).

Input: n = 2 , grid = [[1, 0] , [1, 0]]
Output: []
Explanation: There is no path that rat can choose to travel from (0,0) to (1,1).
"""

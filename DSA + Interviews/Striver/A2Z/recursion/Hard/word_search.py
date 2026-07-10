word = "ABCB"

matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

def helper(matrix, word, row, col, index, visited):
    if index == len(word):
        return True
    
    if ((row, col) in visited or
        row < 0 or row >= len(matrix) or
        col < 0 or col >= len(matrix[0]) or
        matrix[row][col] != word[index]):
        return False
    
    visited.add((row, col))
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        
        if helper(matrix, word, nr, nc, index + 1, visited):
            return True
        
    visited.remove((row, col))
    
    return False
    
def func(matrix, word):
    ROWS, COLS = len(matrix), len(matrix[0])
    visited = set()
    
    for row in range(ROWS):
        for col in range(COLS):
            if helper(matrix, word, row, col, 0, visited):
                return True
    
    return False

print(func(matrix, word))

"""
Problem Statement: Given an m x n grid of characters board and a string word, return true if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: [["A", "B", "C", "E"], ["S", "F", "C", "S"]["A", "D", "E", "E"]] word = "ABCCED"
Output: true
Explanation: We can easily find the given word in the matrix.

Input:[["A", "B", "C", "E"],["S", "F", "C", "S"],["A", "D", "E", "E"]]word = "ABCB"
Output: false
Explanation:  There is no such word in the given matrix.
"""

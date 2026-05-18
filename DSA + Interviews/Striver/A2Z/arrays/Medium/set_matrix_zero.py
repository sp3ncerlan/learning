"""
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Input: matrix=[[1,1,1],
               [1,0,1],
               [1,1,1]]
Output: [[1,0,1]
        ,[0,0,0]
        ,[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

BRUTE FORCE:
- check each row to see if a zero exists, and then go back and set all of that row to a placeholder like -1 so that we don't mistakingly think another row or col is 0
- O(m * n * (m + n)), O(1)

BETTER:
- keep two tracker arrays, one for which rows need to be zeroed and which cols need to be zeroed
- second pass, zero out all marked rows and cols
- improves time at the cost of space
- O(m * n), O(m + n)

OPTIMAL:
- track firstRowZero and firstColZero to see if we needed to have the first row/first col be all zero from the start
- mark zeros in the first row and col for any zeroes found in the matrix
- second pass sets row and cols to zero based on the markers
- handle the first row and col separately based on the flags
- O(m * n), O(1)
"""

# def set_matrix_zero(nums) -> int:

def set_matrix_zero(matrix) -> int:
    m, n = len(matrix), len(matrix[0])
    first_row_zero, first_col_zero = False, False
    # check first row and col
    for row in range(m):
        if matrix[row][0] == 0:
            first_col_zero = True
    
    for col in range(n):
        if matrix[0][col] == 0:
            first_row_zero = True
    
    # check rest of matrix
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
                
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0
                
    if first_row_zero:
        for col in range(n):
            matrix[0][col] = 0
    
    if first_col_zero:
        for row in range(m):
            matrix[row][0] = 0
    
    return matrix

matrix=[[1,1,1], [1,0,1], [1,1,1]]

print(set_matrix_zero(matrix))

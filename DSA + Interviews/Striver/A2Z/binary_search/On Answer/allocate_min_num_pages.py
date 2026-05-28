from itertools import permutations
import math

arr = [25, 46, 28, 49, 24]
m = 4

def students_allocated(arr, pages):
    students_allocated = 1
    current_student_pages = 0
    
    for page_count in arr:
        if current_student_pages + page_count <= pages:
            current_student_pages += page_count
        else:
            students_allocated += 1
            current_student_pages = page_count
            
    return students_allocated

def func(arr, m):
    if len(arr) < m:
        return -1
    
    left, right = max(arr), sum(arr)
    optimal = -1
    while left <= right:
        pages = (left + right) // 2
        
        if students_allocated(arr, pages) <= m:
            optimal = pages
            right = pages - 1
        else:
            left = pages + 1
            
    return optimal
        
print(func(arr, m))

"""
Problem Statement: Given an array 'arr of integer numbers, 'ar[i]' represents the number of pages in the 'i-th' book. There are a 'm' number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

- Each student gets at least one book.
- Each book should be allocated to only one student.
- Book allocation should be in a contiguous manner.

You have to allocate the book to 'm' students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

Example 1:
Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.


Example 2:
Input Format:
 n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
Result:
 71
Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

- arr[i] represents # of pages in the i-th book [25] -> 25 pages in 0th book
- m number of students
- allocate all books to students

- total num of pages / m students, then shrink bounds

BF:
- check if len(arr) < m, then its impossible, return -1
- we can check all page allocations from max(books) to sum(books)
    - this is because we want to save at least an ability to assign each book to one person at least, and then improve from there

OPTIMAL:

"""

student = [1, 2]
cookie = [1, 2, 3]

"""
Problem Statement: Consider a scenario where a teacher wants to distribute cookies to students, with each student receiving at most one cookie. Given two arrays, student and cookie, the ith value in the student array describes the minimum size of cookie that the ith student can be assigned. The jth value in the cookie array represents the size of the jth cookie. If cookie[j] >= student[i], the jth cookie can be assigned to the ith student. Maximize the number of students assigned with cookies and output the maximum number.

Input : Student = [1, 2, 3] , Cookie = [1, 1]
Output :1
Explanation : Only the first cookie (1) satisfies the first student (1), therefore only 1 student is content.

Input : Student = [1, 2] , Cookie = [1, 2, 3]
Output : 2
Explanation : Cookie 1 satisfies student 1 and cookie 2 satisfies student 2. Therefore, 2 students are content.
"""

def func(student, cookie):
    m, n = len(student), len(cookie)
    i, j = 0, 0

    while i < m and j < n:
        minimum = student[i]
        size = cookie[j]

        if size >= minimum:
            i += 1
            j += 1
        else:
            j += 1

    return i

print(func(student, cookie))

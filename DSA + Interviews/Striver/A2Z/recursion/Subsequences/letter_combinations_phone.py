digits = "3"

def recurse(letter_to_digit, digits, i, path, result):
    if i == len(digits):
        result.append(path)
        return

    for letter in letter_to_digit[digits[i]]:
        recurse(letter_to_digit, digits, i + 1, path + letter, result)
    
def func(digits):
    if not digits:
        return []
    
    letter_to_digit = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
        
    result = []
    
    recurse(letter_to_digit, digits, 0, "", result)
    
    return result

print(func(digits))

"""
Problem Statement: Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.

Example 1:
Input:
 digits = "34"
Output:
 [ "dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi" ]
Explanation:
The 3 is mapped with "def" and 4 is mapped with "ghi".  
So all possible combinations by replacing the digits with characters are shown in the output.

Example 2:
Input:
 digits = "3"
Output:
 [ "d", "e", "f" ]
Explanation:
The 3 is mapped with "def".
"""

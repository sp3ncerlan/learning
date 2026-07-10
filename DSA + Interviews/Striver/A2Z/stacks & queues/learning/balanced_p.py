s = "[()"
    
def func(s):
    p_dict = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    
    stack = []
    
    for char in s:
        if char not in p_dict:
            if not stack or p_dict[stack[-1]] != char:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)
            
    return not stack

print(func(s))

"""
Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.

Note:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: str = “( )[ { } ( ) ]”
Output: True
Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.


Example 2:
Input: str = “[ ( )”
Output: False
Explanation: As '[' does not have ']' hence it is not valid and will return false.
"""

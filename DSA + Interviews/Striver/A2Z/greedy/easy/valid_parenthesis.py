"""
Problem Statement: Find the validity of an input string s that only contains the letters '(', ')' and '*'. A string entered is legitimate if

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Input :s = (*))
Output : True
Explanation :The * can be replaced by an opening '(' bracket. The string after replacing the * mark is "(())" and is a valid string.

Input : s = *(()
Output :false
Explanation :The * replaced with any bracket does not form a valid string.
"""
s = "(*))"

def func(s):
    min_open, max_open = 0, 0

    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        else:
            min_open -= 1
            max_open += 1

        if min_open < 0:
            min_open = 0

        if max_open < 0:
            return False

    return min_open == 0

print(func(s))
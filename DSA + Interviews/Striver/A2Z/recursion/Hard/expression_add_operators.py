from collections import defaultdict

num = "123"
target = 6

def func(num, target):
    # need to try all operators for all paths
    ans = []
    
    def recurse(path, current_total, last_operand, index):
        if index == len(num):
            if current_total == target:
                ans.append(path)
            return
        
        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break
            
            part_str = num[index : i + 1]
            current_value = int(part_str)
            
            if index == 0:
                recurse(part_str, current_value, current_value, i + 1)
            else:
                recurse(
                    path + "*" + part_str,
                    current_total - last_operand + (last_operand * current_value),
                    last_operand * current_value,
                    i + 1
                )
                
                recurse(
                    path + "+" + part_str,
                    current_total + current_value,
                    current_value,
                    i + 1
                )
                
                recurse(
                    path + "-" + part_str,
                    current_total - current_value,
                    -current_value,
                    i + 1
                )
        
    recurse("", 0, 0, 0)
    return ans
    
print(func(num, target))

"""
Problem Statement: Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Note that a number can contain multiple digits.

Example 1:
Input:
 num = "123", target = 6
Output:
 ["1*2*3","1+2+3"]
Explanation:
Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input:
 num = "232", target = 8
Output:
 ["2*3+2","2+3*2"]
Explanation:
Both "2*3+2" and "2+3*2" evaluate to 8.
"""

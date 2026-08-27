"""
Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.

Note: We can either take the item as a whole or break it into smaller units.

Example 1:
Input:
 val = [60, 100, 120], wt = [10, 20, 30], capacity = 50  
Output:
 240.000000  
Explanation:

- Take item 0 (w = 10, v = 60)  
- Take item 1 (w = 20, v = 100)  
- Take 2⁄3 of item 2 (w = 20, v = 80)  
Total value = 60 + 100 + 80 = 240

Example 2:
Input:
 val = [60, 100], wt = [10, 20], capacity = 50
Output:
 160.000000
Explanation:

Both items fit entirely since total weight 10 + 20 = 30 ≤ 50.  
Total value = 60 + 100 = 160
"""
bills = [5, 5, 10, 10, 20]

def func(bills):
    fives, tens = 0, 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False

    return True

print(func(bills))

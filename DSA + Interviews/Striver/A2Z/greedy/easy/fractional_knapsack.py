student = [1, 2]
cookie = [1, 2, 3]

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
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

def func(val, wt, capacity):
    val_and_wt = []
    for i in range(len(val)):
        val_and_wt.append((val[i], wt[i]))

    val_and_wt.sort(key=lambda x: x[0] / x[1], reverse=True)

    ans = 0
    i = 0
    while capacity > 0 and i < len(val_and_wt):
        val, wt = val_and_wt[i]

        if wt <= capacity:
            capacity -= wt
            ans += val
        else:
            fraction = capacity / wt
            capacity = 0
            ans += fraction * val

        i += 1

    return ans

print(func(val, wt, capacity))

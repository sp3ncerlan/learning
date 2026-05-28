"""
Problem Statement: You are given 'N' roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day. You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet. Find the minimum number of days required to make at least 'm' bouquets each containing 'k' roses. Return -1 if it is not possible.

Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Example 2:
Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
Result: -1
Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.
"""
N, arr = 8, [7, 7, 7, 7, 13, 11, 12, 7]
bouquets_needed, flowers_in_each_bouquet = 2, 3

def count_bouquets(arr, day, bouquets_needed, flowers_in_each_bouquet):
    bouquets = 0
    
    bunch = 0
    for flower in arr:
        if flower <= day:
            bunch += 1
            if bunch == flowers_in_each_bouquet:
                bouquets += 1
                bunch = 0
        else:
            bunch = 0
            
    return bouquets >= bouquets_needed

def find_days(arr, bouquets_needed, flowers_in_each_bouquet):
    needed_flowers = bouquets_needed * flowers_in_each_bouquet
    if needed_flowers > len(arr):
        return -1

    left = min(arr)
    right = max(arr)
    
    min_days = -1
    while left <= right:
        current_day = (left + right) // 2
        
        if count_bouquets(arr, current_day, bouquets_needed, flowers_in_each_bouquet):
            min_days = current_day
            right = current_day - 1
        else:
            left = current_day + 1
    
    return min_days

print(find_days(arr, bouquets_needed, flowers_in_each_bouquet))

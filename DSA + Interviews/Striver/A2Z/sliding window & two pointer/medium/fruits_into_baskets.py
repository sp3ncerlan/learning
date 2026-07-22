fruits = [1, 2, 3, 2, 2]

def func(fruits):
    fruit_map = {}
    max_fruits = 0
    
    left = 0
    for right in range(len(fruits)):
        right_fruit = fruits[right]
        fruit_map[right_fruit] = fruit_map.get(right_fruit, 0) + 1
        
        while len(fruit_map) > 2:
            left_fruit = fruits[left]
            fruit_map[left_fruit] -= 1
            if fruit_map[left_fruit] == 0:
                del fruit_map[left_fruit]
            left += 1
        
        # calc
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits

print(func(fruits))

"""
Better approach:
- sliding window
- hashmap that keeps track of fruit frequency
    - the size of hashmap has to be 2 to signify 2 baskets
- once we have a size of > 2, then we shrink left and decrement while we have more than 3 in the hashmap

optimal:
- same as better approach, but keep an index as well to see when the last place we saw that fruit was, so we can skip and jump right to the next index

Problem Statement: There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
The goal is to gather as much fruit as possible, adhering to the owner's stringent rules :

There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
Once reaching a tree with fruit that cannot fit into any basket, stop.
Return the maximum number of fruits that can be picked.

Input :fruits = [1, 2, 1]
Output :3
Explanation : We will start from first tree.
The first tree produces the fruit of kind '1' and we will put that in the first basket.
The second tree produces the fruit of kind '2' and we will put that in the second basket.
The third tree produces the fruit of kind '1' and we have first basket that is already holding fruit of kind '1'. So we will put it in first basket.
Hence we were able to collect total of 3 fruits.


Input : fruits = [1, 2, 3, 2, 2]
Output : 4
Explanation : we will start from second tree.
The first basket contains fruits from second , fourth and fifth.
The second basket will contain fruit from third tree.
Hence we collected total of 4 fruits.
"""

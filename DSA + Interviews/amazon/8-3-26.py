"""
Problem: Circular Warehouse Balancing

You are given an array `warehouses` where warehouses[i] represents the number
of packages at warehouse i.

The warehouses are arranged in a circle, meaning the first and last warehouses
are connected.

Your goal is to make every warehouse contain the same number of packages.

Rules:
- You may move packages between warehouses.
- All packages must move in the same direction:
    - either clockwise
    - or counterclockwise
- Moving one package between adjacent warehouses costs 1.

Return the minimum total cost required to make all warehouses equal.

Example:

Input:
warehouses = [3, 4, 6, 6, 6]

Total packages = 25
Target is not an integer, so assume valid test cases only.

Function:
minimumCost(warehouses)

Constraints:
1 <= len(warehouses) <= 100000
0 <= warehouses[i] <= 10^9
"""


def calculate_cost(surplus, deficit, n, direction):
    cost = 0

    i, j = 0, 0
    while i < len(surplus) and j < len(deficit):
        s_index, s_count = surplus[i]
        d_index, d_count = deficit[j]

        if direction == "clockwise":
            distance = (d_index - s_index + n) % n
        else:
            distance = (s_index - d_index + n) % n

        move = min(s_count, d_count)
        cost += distance * move

        surplus[i][1] -= move
        deficit[j][1] -= move

        if surplus[i][1] == 0:
            i += 1

        if deficit[j][1] == 0:
            j += 1

    return cost

def minimumCost(warehouses):
    n = len(warehouses)

    total = sum(warehouses)
    target = total // n

    surplus = []
    deficit = []

    for i, amount in enumerate(warehouses):
        diff = amount - target

        if diff > 0:
            surplus.append([i, diff])
        elif diff < 0:
            deficit.append([i, -diff])

    clockwise_cost = calculate_cost(
        [x[:] for x in surplus],
        [x[:] for x in deficit],
        n,
        direction="clockwise"
    )

    print(surplus)
    print(deficit)

    counter_clockwise_cost = calculate_cost(
        [x[:] for x in surplus],
        [x[:] for x in deficit],
        n,
        direction="counterclockwise"
    )

    return min(clockwise_cost, counter_clockwise_cost)

if __name__ == "__main__":
    warehouses = [3, 4, 6, 6, 6]
    print(minimumCost(warehouses))
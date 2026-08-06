cardScore = [5, 4, 1, 8, 7, 1, 3]
k = 3

"""
- can only take from front or back
- try all combinations, (0, 3), (1, 2), (2, 1), (3, 0)
"""

def func(cardScore, k):
    if k > len(cardScore):
        return 0

    n = len(cardScore)
    total = sum(cardScore[:k])
    score = total

    for i in range(k):
        total -= cardScore[k - i - 1]
        total += cardScore[n - i - 1]

        score = max(score, total)

    return score

print(func(cardScore, k))
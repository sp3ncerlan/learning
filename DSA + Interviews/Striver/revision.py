# Vertical Order Traversal of a Binary Tree
#
# Given the root of a binary tree, return its vertical order traversal.
# Nodes are grouped by their vertical column from left to right. Within
# each column, nodes are ordered from top to bottom. If multiple nodes are
# at the same position, order them by value.
#
# Example tree:
#             1
#           /   \
#          2     3
#         / \   / \
#        4  10 9  10
#         \
#          5
#           \
#            6
#
# Expected output: [[4], [2, 5], [1, 9, 10, 6], [3], [10]]

from collections import deque


# Node structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

"""
- utilize two maps to group by { vertical_index: { row_index: [list of values] } 
"""
# Solution class
class Solution:
    def findVertical(self, root):
        # Group nodes by column, then order them by row and value.
        mapping = {} # { vertical_index: { row_index: [list of values] }
        queue = deque([(root, 0)])
        row = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, v_index = queue.popleft()

                if v_index not in mapping:
                    mapping[v_index] = {}

                if row not in mapping[v_index]:
                    mapping[v_index][row] = []

                mapping[v_index][row].append(node.data)

                if node.left:
                    queue.append((node.left, v_index - 1))
                if node.right:
                    queue.append((node.right, v_index + 1))

            row += 1

        ans = []
        for _, row_dict in sorted(mapping.items()):
            column = []
            for _, values in sorted(row_dict.items()):
                column.extend(sorted(values))
            ans.append(column)

        return ans

# Helper function to print the result
def printResult(result):
    if result:
        for column in result:
            print(" ".join(map(str, column)))
    print()


# Driver
def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    solution = Solution()
    result = solution.findVertical(root)

    print("Vertical Traversal:")
    printResult(result)


main()

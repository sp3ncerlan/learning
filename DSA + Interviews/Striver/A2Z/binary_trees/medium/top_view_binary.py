# Class representing a single node of the binary tree
from collections import deque

class Node:
    # Constructor to initialize node with value
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Class containing the logic for top view
class Solution:
    # Function to return the top view of the binary tree
    def topView(self, root):
        if not root:
            return []

        mapping = {} # { col : value }

        queue = deque([(root, 0)]) # (node, index we are currently trying to insert

        while queue:
            node, col_index = queue.popleft()

            if col_index not in mapping:
                mapping[col_index] = node.data

            if node.left:
                queue.append((node.left, col_index - 1))

            if node.right:
                queue.append((node.right, col_index + 1))

        ans = []
        for col, value in sorted(mapping.items()):
            ans.append(value)

        return ans

# Driver code
if __name__ == "__main__":
    # Create the sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    # Create Solution object
    solution = Solution()

    # Get the top view
    result = solution.topView(root)

    # Print the result
    print("Top View Traversal:", *result)

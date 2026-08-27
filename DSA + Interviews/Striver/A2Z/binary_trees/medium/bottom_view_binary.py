from queue import Queue
from collections import deque, defaultdict


# Node class to represent the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# this time, we just replace what we need to since we're going level by level, end value will be the bottom-most
class Solution:
    def bottomView(self, root):
        if not root:
            return []

        mapping = {} # { col : value }

        queue = deque([(root, 0)]) # (node, column to replace value)

        min_col = max_col = 0

        while queue:
            node, col_index = queue.popleft()
            mapping[col_index] = node.data
            min_col = min(min_col, col_index)
            max_col = max(max_col, col_index)

            if node.left:
                queue.append((node.left, col_index - 1))

            if node.right:
                queue.append((node.right, col_index + 1))

        ans = [mapping[col] for col in range(min_col, max_col + 1)]
        return ans

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(11)
root.right.left = Node(9)

# Creating a Solution object
solution = Solution()

# Get the Bottom View traversal
bottomView = solution.bottomView(root)

# Print the result
print("Bottom View Traversal:")
for node in bottomView:
    print(node, end=" ")

# This class defines a node in the binary tree
from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# This class contains the solution logic
class Solution:
    # Function to perform vertical order traversal
    def findVertical(self, root):
        mapping = {} # { col : { row : values }}

        queue = deque([(root, 0, 0)]) # (node, col, row)

        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                node, col, row  = queue.popleft()

                if col not in mapping:
                    mapping[col] = {}
                if row not in mapping[col]:
                    mapping[col][row] = []

                mapping[col][row].append(node.data)

                if node.left:
                    queue.append((node.left, col - 1, row + 1))

                if node.right:
                    queue.append((node.right, col + 1, row + 1))

        ans = []
        for col in sorted(mapping.keys()):
            col_level = []
            for row in sorted(mapping[col].keys()):
                col_level.extend(sorted(mapping[col][row])) # list of sorted values for this col
            ans.append(col_level)
        return ans

# Function to print result
def printResult(result):
    for level in result:
        print(" ".join(map(str, level)))
    print()

# Driver code
if __name__ == "__main__":
    # Create sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    # Create solution object
    solution = Solution()

    # Call function
    verticalTraversal = solution.findVertical(root)

    # Print result
    print("Vertical Traversal:")
    printResult(verticalTraversal)

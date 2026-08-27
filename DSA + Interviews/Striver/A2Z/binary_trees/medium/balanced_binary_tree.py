# Node class to represent a node in a binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:

    # Function to check if a binary tree is balanced
    def isBalanced(self, root):
        return self.dfsHeight(root) != -1

    # Recursive function to calculate the height of the tree
    def dfsHeight(self, root):
        if not root:
            return 0

        left = self.dfsHeight(root.left)

        if left == -1:
            return -1

        right = self.dfsHeight(root.right)

        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

# Driver code
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Checking if the tree is balanced
    if solution.isBalanced(root):
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")

# Class to represent a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to count nodes in a complete binary tree
    def countNodes(self, root):
        if not root:
            return 0

        left = self.findHeightLeft(root)
        right = self.findHeightRight(root)

        if left == right:
            return (2 ** left) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Helper to find height from leftmost path
    def findHeightLeft(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # Helper to find height from rightmost path
    def findHeightRight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

# Driver code
if __name__ == "__main__":
    # Create binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    # Create solution object
    sol = Solution()

    # Count total nodes
    totalNodes = sol.countNodes(root)

    # Output result
    print("Total number of nodes in the Complete Binary Tree:", totalNodes)

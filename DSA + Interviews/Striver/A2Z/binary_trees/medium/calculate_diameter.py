
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to find the diameter of the binary tree
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        self.height(root, diameter)

        return diameter

    # Function to calculate the height of the tree and update the diameter
    def height(self, node, diameter):
        if not node:
            return 0

        left = self.height(node.left, diameter)
        right = self.height(node.right, diameter)

        diameter[0] = max(diameter[0], (left + right + 1))

        return 1 + max(left, right)

# Main function
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

    # Calculate the diameter of the binary tree
    diameter = solution.diameterOfBinaryTree(root)

    print("The diameter of the binary tree is:", diameter)

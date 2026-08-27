# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val  # Data stored in the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

class Solution:
    # Function to check if two binary trees are identical
    def isIdentical(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.data != node2.data:
            return False

        return self.isIdentical(node1.left, node2.left) and self.isIdentical(node1.right, node2.right)

# Driver code
if __name__ == "__main__":
    # Creating the first binary tree (Node1)
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    # Creating the second binary tree (Node2)
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)

    # Creating an instance of the Solution class
    solution = Solution()

    # Check if the two binary trees are identical and output the result
    if solution.isIdentical(root1, root2):
        print("The binary trees are identical.")
    else:
        print("The binary trees are not identical.")

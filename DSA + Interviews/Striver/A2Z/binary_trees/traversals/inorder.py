# Node structure for
# the binary tree
class Node:
    # Constructor to initialize
    # the node with a value
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Solution class to perform preorder traversal
class Solution:

    # Function to perform preorder traversal
    # of the tree and store values in 'arr'
    def inorder(self, root, arr):
        if not root:
            return

        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def inOrder(self, root):
        arr = []

        self.inorder(root, arr)

        return arr

# Main function
if __name__ == "__main__":

    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting inorder traversal
    sol = Solution()
    result = sol.inOrder(root)

    # Displaying the preorder traversal result
    print("Inorder Traversal: ", end="")
    # Output each value in the
    # preorder traversal result
    for val in result:
        print(val, end=" ")
    print()

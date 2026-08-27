# Define a TreeNode class for the binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x  # The value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Function to perform preorder traversal of a binary tree iteratively
def preorderTraversal(root):
    preorder = []

    stack = [root]
    while stack:
        node = stack.pop()

        preorder.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return preorder

# Driver code
if __name__ == "__main__":
    # Creating a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Getting the preorder traversal
    result = preorderTraversal(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal:", result)
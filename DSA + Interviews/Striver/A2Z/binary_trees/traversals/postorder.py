# Define a TreeNode class for the binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x  # The value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Function to perform postorder traversal of a binary tree iteratively
def postOrder(root):
    postorder = []
    last_visited = None
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek_node = stack[-1]
            if peek_node.right and peek_node.right != last_visited:
                curr = peek_node.right
            else:
                postorder.append(peek_node.val)
                last_visited = stack.pop()

    return postorder

# Driver code
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Getting the postorder traversal
    result = postOrder(root)

    # Displaying the postorder traversal result
    print("Postorder traversal:", result)
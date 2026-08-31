class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def changeTree(self, root):
        # top down to change children to equal parent
        if not root:
            return

        child_sum = 0
        if root.left:
            child_sum += root.left.val
        if root.right:
            child_sum += root.right.val

        if child_sum >= root.val:
            root.val = child_sum
        else:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val

        # bottom-up to confirm
        self.changeTree(root.left)
        self.changeTree(root.right)

        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val

        if root.left or root.right:
            root.val = total

# Function to print the inorder
# traversal of the tree
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)


# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()

# Print the inorder traversal
# of tree before modification
print("Binary Tree before modification:", end=" ")
inorderTraversal(root)
print()

# Call the changeTree function
# to modify the binary tree
sol.changeTree(root)

# Print the inorder traversal
# after modification
print("Binary Tree after Children Sum Property:", end=" ")
inorderTraversal(root)
print()

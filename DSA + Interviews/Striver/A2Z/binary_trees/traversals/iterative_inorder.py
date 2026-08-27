# Define the TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Solution:
    # Function to perform inorder traversal
    # of a binary tree iteratively
    def inorder(self, root):
        inorder = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            inorder.append(curr.data)

            curr = curr.right

        return inorder

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the inorder traversal
result = sol.inorder(root)

# Displaying the inorder traversal result
print("Inorder Traversal:", result)

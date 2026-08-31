# TreeNode structure
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Solution class
class Solution:
    def buildTree(self, preorder, inorder):
        mapping = {val: idx for idx, val in enumerate(inorder)} # { inorder node : index }

        # Helper function to build tree recursively
        def build(preorder, inorder):
            if len(inorder) == 1:
                node = 

# Inorder print
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Driver
if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()

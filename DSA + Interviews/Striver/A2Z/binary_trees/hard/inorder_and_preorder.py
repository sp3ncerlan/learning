# TreeNode structure
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Solution class
class Solution:
    def buildTree(self, preorder, inorder):
        # Create a hashmap to store inorder indices
        # Use recursion to build the tree from preorder and inorder
        pass


# Inorder traversal
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)


# Driver
def main():
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()


main()

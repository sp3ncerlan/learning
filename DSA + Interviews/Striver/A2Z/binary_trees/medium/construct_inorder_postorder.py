# Construct Binary Tree from Inorder and Postorder Traversal
#
# Given two integer arrays, inorder and postorder, where inorder is the
# inorder traversal of a binary tree and postorder is the postorder
# traversal of the same tree, construct and return the binary tree.
#
# You may assume that all values are unique and that both traversals are
# valid representations of the same tree.
#
# Example:
# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
# Output tree: [3, 9, 20, null, null, 15, 7]

# TreeNode structure
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
- postorder means iterate from the back
"""
# Solution class
class Solution:
    def buildTree(self, inorder, postorder):
        # Build the binary tree from inorder and postorder traversals.
        mapping = {val: idx for idx, val in enumerate(inorder)}
        post_index = len(postorder) - 1

        def build(inStart, inEnd):
            nonlocal post_index

            if inStart > inEnd:
                return None

            root_value = postorder[post_index]
            root = TreeNode(root_value)
            post_index -= 1

            inRoot = mapping[root_value]

            root.right = build(inRoot + 1, inEnd)
            root.left = build(inStart, inRoot - 1)

            return root

        return build(0, len(inorder) - 1)

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
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)

    print("Inorder of Binary Tree Created:")
    printInorder(root)
    print()


main()

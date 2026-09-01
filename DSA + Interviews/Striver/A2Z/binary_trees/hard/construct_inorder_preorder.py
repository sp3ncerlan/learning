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
        pre_index = 0

        # Helper function to build tree recursively
        def build(inStart, inEnd):
            nonlocal pre_index
            if inStart > inEnd:
                return None

            root_val = preorder[pre_index]
            root = TreeNode(root_val)
            pre_index += 1

            inRoot = mapping[root_val]

            root.left = build(inStart, inRoot - 1)
            root.right = build(inRoot + 1, inEnd)

            return root

        return build(0, len(inorder) - 1)

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

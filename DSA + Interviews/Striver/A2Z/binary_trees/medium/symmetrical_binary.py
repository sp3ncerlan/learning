class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left_node: TreeNode, right_node: TreeNode) -> bool:
        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        if left_node.val != right_node.val:
            return False

        return (self.isMirror(left_node.left, right_node.right) and self.isMirror(left_node.right, right_node.left))

# Driver code
if __name__ == "__main__":
    # Symmetric Tree Example:
    #        1
    #      /   \
    #     2     2
    #    / \   / \
    #   3   4 4   3
    symmetric_root = TreeNode(1)
    symmetric_root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    symmetric_root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    # Asymmetric Tree Example:
    #        1
    #      /   \
    #     2     2
    #      \     \
    #       3     3
    asymmetric_root = TreeNode(1)
    asymmetric_root.left = TreeNode(2, None, TreeNode(3))
    asymmetric_root.right = TreeNode(2, None, TreeNode(3))

    sol = Solution()
    print("Is Symmetric Tree Symmetric?", sol.isSymmetric(symmetric_root))   # Expected: True
    print("Is Asymmetric Tree Symmetric?", sol.isSymmetric(asymmetric_root)) # Expected: False
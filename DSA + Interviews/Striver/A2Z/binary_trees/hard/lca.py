# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return None

if __name__ == "__main__":
    # Construct a simple binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    solution = Solution()
    p = root.left  # Node with value 5
    q = root.right  # Node with value 1

    lca = solution.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.data)
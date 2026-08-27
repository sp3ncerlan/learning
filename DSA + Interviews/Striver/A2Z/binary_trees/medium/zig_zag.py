from collections import deque

# Class to represent a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x          # Value of the node
        self.left = None      # Pointer to left child
        self.right = None     # Pointer to right child

class Solution:
    # Function to perform zigzag (spiral) level order traversal
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        flag = True
        res = []

        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            if not flag:
                level.reverse()

            flag = not flag
            res.append(level)

        return res

# Driver code
if __name__ == "__main__":
    # Create binary tree:
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Create solution object
    sol = Solution()

    # Get zigzag traversal
    ans = sol.zigzagLevelOrder(root)

    # Print result
    print(ans)

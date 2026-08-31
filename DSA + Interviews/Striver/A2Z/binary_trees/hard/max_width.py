from collections import deque

# Class definition for binary tree node
class TreeNode:
    # Constructor to initialize node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Class containing the function
class Solution:
    # Function to calculate maximum width
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            queue_length = len(queue)
            min_index = queue[0][1]
            first = 0
            last = 0

            for i in range(queue_length):
                node, index = queue.popleft()

                curr_index = index - min_index

                if i == 0:
                    first = curr_index
                if i == queue_length - 1:
                    last = curr_index

                if node.left:
                    queue.append((node.left, 2 * curr_index + 1))
                if node.right:
                    queue.append((node.right, 2 * curr_index + 2))

            max_width = max(max_width, last - first + 1)

        return max_width

# Driver code
if __name__ == "__main__":

    # Build the tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    # Create object
    sol = Solution()

    # Print the result
    print("Maximum width:", sol.widthOfBinaryTree(root))

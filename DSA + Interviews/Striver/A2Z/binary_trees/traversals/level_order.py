from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    # Function to perform level-order traversal of a binary tree
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            queueLength = len(queue)
            level = []

            for _ in range(queueLength):
                node = queue.popleft()
                level.append(node.data)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res

# Function to print the elements of a list
def printList(lst):
    # Iterate through the list and print each element
    for num in lst:
        print(num, end=' ')
    print()


# Main function to test the level-order traversal
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")
    # Printing the level order traversal result
    for level in result:
        printList(level)
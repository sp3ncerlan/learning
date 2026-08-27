# TreeNode class for Binary Tree
class TreeNode:
    def __init__(self, val):
        # Initialize node with value
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Function to find the path from root to a given node
    def getPath(self, root, arr, x):
        if not root:
            return False

        arr.append(root.val)

        if root.val == x:
            return True

        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        arr.pop()
        return False

    # Function to return the final path list
    def solve(self, root, x):
        path = []
        if not root:
            return path
        self.getPath(root, path, x)
        return path

# Main driver function
def main():
    # Construct the tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Create solution object
    sol = Solution()

    # Target node value
    target = 7

    # Get path
    path = sol.solve(root, target)

    # Print result
    print(f"Path from root to node {target}:", end=" ")
    for i in range(len(path)):
        print(path[i], end="")
        if i < len(path) - 1:
            print(" -> ", end="")

main()

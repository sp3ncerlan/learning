"""
Problem Statement: Given the root of a Binary Tree, return the preorder, inorder and postorder traversal sequence of the given tree by making just one traversal.
"""
# Node structure for the binary tree
class Node:
    # Constructor to initialize the node with a value
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class containing the traversal function
class Solution:
    # Function to get the Preorder,
    # Inorder and Postorder traversal
    # Of Binary Tree in One traversal
    def preInPostTraversal(self, root):
        preorder = []
        inorder = []
        postorder = []

        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()

            # preorder
            if state == 1:
                preorder.append(node.data)
                stack.append((node, 2))

                if node.left:
                    stack.append((node.left, 1))
            # inorder
            elif state == 2:
                inorder.append(node.data)
                stack.append((node, 3))

                if node.right:
                    stack.append((node.right, 1))
            # postorder
            else:
                postorder.append(node.data)

        return [preorder, inorder, postorder]

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Create object of Solution class
    sol = Solution()

    # Getting the traversals
    traversals = sol.preInPostTraversal(root)

    # Extracting and printing the traversals
    pre = traversals[0]
    ino = traversals[1]
    post = traversals[2]

    print("Preorder traversal:", *pre)
    print("Inorder traversal:", *ino)
    print("Postorder traversal:", *post)

from collections import deque

# Function to perform in-order traversal and print the tree
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def serialize(self, root):
        if not root:
            return ""

        ans = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()

                if not curr:
                    ans.append("#")
                else:
                    ans.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)

        return "".join(ans)

    def deserialize(self, data):
        if len(data) == 0:
            return None

        root = TreeNode(data[0])
        index = 1
        queue = deque([root])
        while queue:
            parent = queue.popleft()

            if index < len(data) and data[index] != "#":
                parent.left = TreeNode(int(data[index]))
                queue.append(parent.left)
            else:
                parent.left = None

            index += 1

            if index < len(data) and data[index] != "#":
                parent.right = TreeNode(int(data[index]))
                queue.append(parent.right)
            else:
                parent.right = None

            index += 1

        return root

# Driver code
if __name__ == "__main__":
    # Manually create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Create object of Solution
    solution = Solution()

    # Print original tree
    print("Orignal Tree: ", end="")
    inorder(root)
    print()

    # Serialize the tree
    serialized = solution.serialize(root)
    print("Serialized:", serialized)

    # Deserialize the tree
    deserialized = solution.deserialize(serialized)
    print("Tree after deserialisation: ", end="")
    inorder(deserialized)
    print()
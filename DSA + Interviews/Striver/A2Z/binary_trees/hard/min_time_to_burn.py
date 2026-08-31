# Definition of a binary tree node
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Main class containing the burning logic
class Solution:
    # Function to calculate minimum time to burn the entire tree from the target node
    def minTime(self, root, target):
        parent_map = {}
        target_node = self.createParentMap(root, target, parent_map)

        queue = deque([target_node])
        visited = {target_node}

        time = 0
        while queue:
            level = len(queue)
            was_burned = False

            for _ in range(level):
                curr = queue.popleft()

                for neighbor in (curr.left, curr.right, parent_map.get(curr)):
                    if neighbor and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        was_burned = True

            if was_burned:
                time += 1

        return time

    def createParentMap(self, root, target_val, parent_map):
        target_node = None

        def dfs(node, parent=None):
            nonlocal target_node
            if not node:
                return

            if node.val == target_val:
                target_node = node

            if parent:
                parent_map[node] = parent

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)
        return target_node

# Driver code
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.right = TreeNode(7)

    target = 1
    sol = Solution()
    print("Minimum time to burn the tree:", sol.minTime(root, target))

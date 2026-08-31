from collections import deque
from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = self.map_parents(root, {})

        return self.bfs_from_target(target, parent_map, k)

    # This method builds a mapping of each node to its parent using BFS
    def map_parents(self, root: TreeNode, parent_map: dict):
        parents = {}

        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        return parents

    # This method performs BFS starting from the target node to find nodes at distance K
    def bfs_from_target(self, target: TreeNode, parent_map: dict, k: int) -> List[int]:
        visited = {target}
        queue = deque([target])
        current_dist = 0

        while queue:
            if current_dist == k:
                return [node.val for node in queue]

            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()

                for neighbor in (curr.left, curr.right, parent_map.get(curr)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            current_dist += 1


        return []

# Constructing the binary tree manually
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# Set the target node and distance
target = root.left  # Node with value 5
k = 2

# Run the solution
sol = Solution()
result = sol.distanceK(root, target, k)

# Print the output
print("Nodes at distance", k, "from target:", result)

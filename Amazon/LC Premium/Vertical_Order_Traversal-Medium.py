# Time Complexity: O(N)
# Space Complexity: O(N)

# This is different from hard problem and when x and y values are same we don't need to sort them as per values
from collections import deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None:
            return result
        mapping = {}
        minimum = 0
        maximum = 0
        queue_for_node = deque()
        queue_for_vertical_level = deque()
        queue_for_node.append(root)
        queue_for_vertical_level.append(0)
        while queue_for_node:
            size = len(queue_for_node)
            for i in range(size):
                current_node = queue_for_node.popleft()
                current_level = queue_for_vertical_level.popleft()
                if current_level not in mapping:
                    mapping[current_level] = []
                mapping[current_level].append(current_node.val)
                if current_node.left:
                    queue_for_node.append(current_node.left)
                    queue_for_vertical_level.append(current_level - 1)
                if current_node.right:
                    queue_for_node.append(current_node.right)
                    queue_for_vertical_level.append(current_level + 1)
        for key in mapping.keys():
            if key < minimum:
                minimum = key
            if key > maximum:
                maximum = key
        for i in range(minimum, maximum + 1):
            result.append(mapping[i])
        return result

        
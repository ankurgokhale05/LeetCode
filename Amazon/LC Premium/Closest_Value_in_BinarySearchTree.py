# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root == None:
            return root
        stack = [(root, False)]
        res = []
        while stack:
            current, visited = stack.pop()
            if current:
                if visited:
                    res.append(current.val)
                else:
                    stack.append((current.right, False))
                    stack.append((current, True))
                    stack.append((current.left, False))
        min_diff = float('inf')
        for i in range(len(res)):
            diff = abs(target - res[i])
            min_diff = min(diff, min_diff)
        for i in range(len(res)):
            if abs(target - res[i]) == min_diff:
                return res[i]
            
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest 
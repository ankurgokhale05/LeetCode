# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
See Most Voted 2nd solution

'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = float('-inf')
        def get_max_gain(node: TreeNode):
            nonlocal max_path_sum
            if not node:
                return 0
            max_left_gain = max(get_max_gain(node.left),0)
            max_right_gain = max(get_max_gain(node.right),0)
            
            current_max_path = node.val + max_left_gain + max_right_gain
            max_path_sum = max(max_path_sum, current_max_path)
            return node.val + max(max_left_gain,max_right_gain)
        get_max_gain(root)
        return max_path_sum
            
        
        
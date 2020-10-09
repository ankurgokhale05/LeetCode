# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
There can be 3 possible cases:
1) The longest path can be sum of left_height + right_height
2) The longest path can be within subtree of left tree
3) The longest path can be within subtree of right tree
Time Complexity : O(n) we visit every node once
Space Complexity: O(n) we call callstack n times during DFS or recursion.
'''

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(left_height + right_height, max(left_diameter, right_diameter))
    
    def height(self, root:TreeNode):
        if root == None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))
        
        
        
        
        
        
        
        
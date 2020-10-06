# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or root == p or root == q:
            return root
        # Doing a post order traversal
        left_ancestor = self.lowestCommonAncestor(root.left,p,q)
        right_ancestor = self.lowestCommonAncestor(root.right,p,q)
        
        if left_ancestor and right_ancestor:
            return root
        if left_ancestor:
            return left_ancestor
        if right_ancestor:
            return right_ancestor
        else:
            return None
        
        
        
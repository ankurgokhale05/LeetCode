# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: Recursion to check at every level of s and whether t exist as a subtree or not
# Time Complexity: O(MN) since we are traversing entire S - tree where M are number of nodes in S and N are number of nodes in T
# Space Complexity : O(min(MN))
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        elif self.isSameTree(s,t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s: TreeNode, t: TreeNode):
        if s == None or t == None:
            return s == None and t == None
        elif s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right,t.right)
        else:
            return False
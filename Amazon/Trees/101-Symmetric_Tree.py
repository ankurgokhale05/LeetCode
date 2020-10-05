# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Time Complexity: O(n) Since we need to traverse all nodes of tree
Space Complexity: O(n) Since we call the function n times 

'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isSame(root.left, root.right)
    def isSame(self, t1: TreeNode, t2: TreeNode):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return t1.val == t2.val and self.isSame(t1.left, t2.right) and self.isSame(t1.right, t2.left)
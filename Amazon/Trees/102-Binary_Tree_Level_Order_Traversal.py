'''
We use BFS and maintain a double ended queue or deque. At every level we iterate over nodes ranging with size of queue. And then add current_level to result for final list
Time Complexity: O(n)
Space Complexity: O(n)
'''

from collections import deque

class Solution(object):
    def levelOrder(self, root: TreeNode):
        if root == None:
            return []
        result = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            current_level = []
            for i in range(size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)
        return result
                
                
                
                
                
                
                
                
                
            
            
            
        
        
        
        
    
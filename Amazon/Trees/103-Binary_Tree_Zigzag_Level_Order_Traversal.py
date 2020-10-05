# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
In this problem we need to traverse binary tree level by level. When we see levels in binary tree, we need to think about bfs, because it is its logic: it first traverse all neighbors, before we go deeper. Here we also need to change direction on each level as well. So, algorithm is the following:

We create queue, where we first put our root.
result is to keep final result and direction, equal to 1 or -1 is direction of traverse.
Then we start to traverse level by level: if we have k elements in queue currently, we remove them all and put their children instead. We continue to do this until our queue is empty. Meanwile we form level list and then add it to result, using correct direction and change direction after.
Complexity:
Time complexity is O(n), where n is number of nodes in our binary tree. 
Space complexity is also O(n), because our result has this size in the end. If we do not count output as additional space, then it will be O(w), where w is width of tree. It can be reduces to O(1) I think if we traverse levels in different order directly, but it is just not worth it.


'''
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = []
        direction = 1
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
            result.append(current_level[::direction])
            direction = direction * -1
        return result
                
        
        
#Time Complexity : O(N)
'''
Intuition is to think of a graph traversal. Therefore here we use BFS and go levelwise and update the count. 
'''

import collections
class Solution:
    def bfs(self, queue, grid):
        weight = 0
        while len(queue) != 0:
            i,j, minutes = queue.popleft()
            weight = max(minutes, weight)
            
            for new_i, new_j in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i = new_i + i
                new_j = new_j + j
                if new_i >=0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j, minutes + 1))
                    
        return weight
        
        
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        minutes = self.bfs(queue, grid)
        
        
        for row in grid:
            if 1 in row:
                return -1
        return minutes
        
                        
        
        
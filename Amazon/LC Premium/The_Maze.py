'''

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
 

Constraints:

1 <= maze.length, maze[i].length <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= maze.length
0 <= startcol, destinationcol <= maze[i].length
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The maze contains at least 2 empty spaces.
'''

# BFS Solution
'''
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if maze == None or len(maze) == 0:
            return False
        queue = deque()
        queue.append((start[0], start[1]))
        maze[start[0]][start[1]] = 2 # marking the starting coordinates as visited
        directions = [(0,1),(0,-1), (1,0),(-1,0)]
        
        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for direction in directions:
                r = x
                c = y
                while r >= 0 and r < len(maze) and c >= 0 and c < len(maze[0]) and maze[r][c] != 1:
                    r += direction[0]
                    c += direction[1]
                    
                # bring it back to stoppage point
                r -= direction[0] 
                c -= direction[1]
                if maze[r][c] != 2:
                    queue.append((r,c))
                    maze[r][c] = 2
        return False
                    
'''
# DFS Solution
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if maze == None or len(maze) == 0:
            return False
        directions = [(0,1),(0,-1), (1,0),(-1,0)]
        return self.dfs(maze, start, destination)
    
    def dfs(self, maze, start, destination):
        # base 
        if maze[start[0]][start[1]] == 2:
            return False
        if start[0] == destination[0] and start[1] == destination[1]:
            return True
        directions = [(0,1),(0,-1), (1,0),(-1,0)]
        # logic
        maze[start[0]][start[1]] = 2
        
        for direction in directions:
            r = start[0]
            c = start[1]
            while r >= 0 and r < len(maze) and c >= 0 and c < len(maze[0]) and maze[r][c] != 1:
                r += direction[0]
                c += direction[1]
            r -= direction[0]
            c -= direction[1]
            if self.dfs(maze, [r,c], destination):
                return True
        return False
                
            

        
        
        
        
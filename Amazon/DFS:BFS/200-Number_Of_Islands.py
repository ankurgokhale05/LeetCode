# DFS Solution
'''
For island grid we do a depth first search and whenever we find an island or 1 we grab that -> increase island count by 1 and check horizontally and vertically for 1 recursively. Be careful to check boundary conditions. 
If you picture a tree structure, a BFS would go root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right, etc, so traversing level by level. A DFS would fill the bottom level first, then traverse back up. DFS is generally a little easier to code, but BFS is a little more intuitive. You would use a BFS when looking for something in a tree that you expect to be near the top, but would use a DFS to find something in a tree that you expect to be near the leaves. BFS will find the shortest path between two items (think maze solving) whereas DFS doesn't guarantee the shortest path.



Time Complexity : O(MN)
Space Complexity Complexity : O(MN)

'''

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        countIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    countIslands+= 1
                    grid[i][j] = 0
                    self.toChangeWater(grid, i, j)
        return countIslands
    
    def toChangeWater(self, grid, i, j):
        if i < 0 or i>= len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == '0':
            return '1'
        grid[i][j] = '0'
        self.toChangeWater(grid, i+1, j)
        self.toChangeWater(grid, i-1, j)
        self.toChangeWater(grid, i, j-1)
        self.toChangeWater(grid, i, j+1)        



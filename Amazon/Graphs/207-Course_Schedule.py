# Use Kahns algorithm basis of Topological Sort.
# Time Complexity : O(V+E)
# Space Complexity: O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = collections.defaultdict(set) # storing indegrees for all nodes
        outdegree = collections.defaultdict(set) # storing outdegrees for all nodes
        
        for x, y in prerequisites:
            outdegree[y].add(x) #for single prerequisite what courses should be taken after that
            indegree[x].add(y) #for all courses what are their prerequisites
            
        connection_removed = 0
        indegree_zero = [] # stack for storing element whose indegree is 0 for it to be removed
        for i in range(numCourses):
            if not indegree[i]:
                indegree_zero.append(i)
                connection_removed += 1
        while indegree_zero:
            node = indegree_zero.pop()
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    indegree_zero.append(x)
                    connection_removed += 1
        return connection_removed == numCourses

        
        
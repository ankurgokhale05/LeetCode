#Method 1 Sorting 
# Time Complexity: O(nlogn)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

#Time Complexity: Min Heap
# Time Complexity: O(nlogk)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap,(dist,x,y))
            else:
                heapq.heappush(heap,(dist,x,y))
        return [[x,y] for (dist,x,y) in heap]
        


        

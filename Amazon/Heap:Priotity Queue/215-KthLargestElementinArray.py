'''
Method 1: Sorting
Time Complexity: O(nlogn)
'''

class Solution:
    def findKthLargest(self, nums:List[int], k: int) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        return nums[k-1]


'''
Method 2: Using heap
Time Complexity: O(nlogk)
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
        
        for i in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
'''   
Method 3: Using inbuilt function of heap
'''
import heapq
class Solution:
    def findKthLargest(self, nums:List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
        
        

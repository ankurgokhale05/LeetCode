'''
#Method 1: Using sorting O(nlogn)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        array = sorted(dict, key = dict.get, reverse = True)
        return array[:k]
    
#Method 2: Using MinHeap
# Time Complexity : O(nlogk)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        output = []
        for v,f in c.items():
            if len(output) < k:
                heapq.heappush(output, [f,v])
            else:
                if f > output[0][0]:
                    heapq.heappop(output)
                    heapq.heappush(output, [f,v])
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(output)[1])
        return res[::-1]
            
                
                
                
        

        

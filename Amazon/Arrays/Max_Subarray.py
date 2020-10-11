# Brute Force
# Compare sum of all possible subarrays and find max_sum
# Time Complexity : O(n^2)
# Space Complexity : O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(len(nums)):
            sums = nums[i]
            max_sum = max(max_sum, sums)
            for j in range(i+1, len(nums)):
                sums += nums[j]
                max_sum = max(max_sum, sums)
        return max_sum
        

'''
Method 2: Kadane's Algorithm.
At each point calculate max of whether to start subarray from that element or append that element to previous subarray. Repeat it multiple times.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = max_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i] + current_sum, nums[i])
            max_sum = max(current_sum, max_sum)
            
        return max_sum
'''
                
                
            
            
            
# Classic Hashset Problem
# The intuition is to use hashset to store all unique numbers and then iterate starting from 0 to len(nums) + 1 and check whether i is in set. If not return the index.  
# len(nums) + 1 - for edge case where nums = [0] so output should be 1.
# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in sets:
                return i

# This is using extra space O(n)
# Now without using extra space
# Use Gaussian law for sums till len(nums) and subtract sum of nums.The resulting sum is missing element
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n* (n+1) // 2 - sum(nums) 
       
            
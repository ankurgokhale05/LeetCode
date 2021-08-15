'''
Find KTH Missing Element in Sorted Array
Time Complexity: O(logN)
Space Complexity: O(1)

'''

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        complete_length = nums[-1] - nums[0] + 1
        missing_nums = complete_length - len(nums)
        
        if k > missing_nums:
            return nums[-1] + (k-missing_nums)
        
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing
            else:
                right = mid
        return nums[left] + k
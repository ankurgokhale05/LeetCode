# Method: Two Pointer
# The idea is to use two pointer to compute complementary pairs. We don't need a hashset as we don't need a lookup for specific target.
#Variation of 3Sum problem
# Time Complexity: O(n^2)
# Space Complexity: O(logn) to O(n) based on what algorithm sorting uses.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[n-1]
        for i in range(len(nums)-2):
            left = i+1
            right = n-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
        return result
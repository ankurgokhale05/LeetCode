#Brute Force
# Time Complexity: O(N^3)
# Space complexity: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and i !=j and i != k and j != k:
                        solution = sorted([nums[i], nums[j], nums[k]])
                        if solution not in result:
                            result.append(solution)
        return result


#The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.
# Method: First sort the array the base condition of i == i-1 and continue our left pointer will be i + 1 and right pointer at end. then use two pointer method. In order to avoid duplicates we check if nums[left] == nums[left+1] and update left pointer if same We do the same for right. And then we check if sum is greater than or less than zero and update the pointers accordingly.
# Time Complexity : O(N^2)
# Space Complexity: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            current_num = nums[i]
            while left < right:
                current_sum = current_num + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([current_num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                if current_sum > 0:
                    right -= 1
                if current_sum < 0:
                    left += 1
        return result

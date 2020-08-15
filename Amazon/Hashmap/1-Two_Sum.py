'''
So we are given array of numbers and a target
Method 1: Brute Force
The brute force approach would be to loop over the array two times and check if the sum of elements of i and j add to the given target
'''
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

'''
Method 2: To use a dictionary and map the elements and difference between the target and elements to store
'''
class Solution:
    def twoSum(self,nums: List[int], target: int):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target - nums[i]] = i
        return nums
 
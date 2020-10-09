#Time Complexity : O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        
#The goal of this search is to find the smallest element of array. 
        while left < right:
            mid = left + (right - left)//2
# Is middle element greater than element to right. Because in a sorted array all element to left are less than element at right. If nums[mid] > target then it is peculiar. We can narrow down search space to left = midpoint +1 and search in right part of array. we do that because we know for sure middle element is not smallest as nums[mid] > nums[right]
# Else it is normal and we search for left part of array.
# Loop will break when left is at smallest element index
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        start = left
        left = 0
        right = len(nums) - 1
# Now since we know the starting index or smallest element. 
        if target >= nums[start] and target <= nums[right]: # Perfect boundaries it since this is sorted version.
# In this case [4,5,6,7,0,1,2] if target is 1 we got nums[start] = 0 nums[left] = 4 and nums[right] = 2. We know that we have to search on right side of nums[start] else on left side of nums[start]
            left = start
        else:
            right = start 
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            
                
                
'''
Method 1 using Space
Idea is to use two arrays that calculate the products from left side and right side. The caveat is that In the left_products array we will take product of all elements that are to the left of that element and same for right product array. Look at LC Solution for diagram. Then we multiply each element of them to get output.
Time Complexity: O(N)
Space Complexity: O(N)

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [0] * len(nums)
        right_product = [0] * len(nums)
        output_arr = [0] * len(nums)
        left_product[0] = 1
        right_product[n-1] = 1
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        for i in range(len(nums)):
            output_arr[i] = left_product[i] * right_product[i]
        return output_arr
'''
Method 2: Without space
Time Complexity: O(N)
Space Complexity: O(1)
We don't have to use left and right product array. The left product array can be obtained by making changes in ouptut_arr itself. For right_product array we can take variable R as 1 and multiply with output_arr value and then update R with nums[i] value.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output_arr = [0] * len(nums)
        output_arr[0] = 1
        R = 1
        for i in range(1,len(nums)):
            output_arr[i] = output_arr[i-1] * nums[i-1]
            
        for i in range(n-1, -1, -1):
            output_arr[i] = output_arr[i] * R
            R = R * nums[i]
        return output_arr
            
        
            
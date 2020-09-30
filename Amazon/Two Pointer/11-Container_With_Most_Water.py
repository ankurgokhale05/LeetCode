# Brute Force Approach
# Time Complextiy: O(N^2)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                smallheight = min(height[i],height[j])
                maxarea = max(maxarea, smallheight * (j-i))
        return maxarea

# Method 2: 
# Use two pointer approach. if value of a_pointer is less than b_pointer then height becomes value of a_pointer else height becomes b_pointer. After that use index subtraction to calculate length.
#You want the pointer that points to maximum height for maximum area. Therefore when comparing the two pointer heights we will move the pointer that corresponding to smaller height among two.
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height:List[int]) -> int:
        maxarea = 0
        a_pointer = 0
        b_pointer = len(height) - 1
        while a_pointer < b_pointer:
            if height[a_pointer] < height[b_pointer]:
                maxarea = max(maxarea, height[a_pointer] * (b_pointer - a_pointer))
                a_pointer += 1
            else:
                maxarea = max(maxarea, height[b_pointer] * (b_pointer - a_pointer))
                b_pointer -= 1
        return maxarea

            
                
        
            
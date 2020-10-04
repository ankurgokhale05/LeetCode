'''
The idea is to compute max-height from both left and right direction. 
when right_max[i] > left_max[i] the water trapped depends on left_max and similarly when left_max[i] > right_max[i] it depends on right_max
 So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.
 
Time Complexity: O(N)
Space Complexity: O(1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if height == None or len(height) == 0:
            return 0
        result = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while(left < right):
            if height[left] < height[right]: 
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left = left + 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right = right - 1
        return result


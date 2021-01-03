'''
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = []
Output: 0
Example 3:

Input: costs = [[7,6,2]]
Output: 2
'''

'''
Brute Force: Exhaustive Search
Time Complexity: O(2^N)



class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs == None or len(costs) == 0:
            return 0
        case1 = self.helper(costs,0,0,0)
        case2 = self.helper(costs,0,1,0)
        case3 = self.helper(costs,0,2,0)
        return min(case1, min(case2, case3))
    
    def helper(self, costs: List[List[int]], row: int, color: int, total_min_cost: int):
        # base
        if row == len(costs):
            return total_min_cost
        # logic
        
        if color == 0:
            return min(self.helper(costs, row+1, 1, total_min_cost + costs[row][0])
            ,self.helper(costs, row+1, 2, total_min_cost + costs[row][0]))
        elif color == 1:
            return min(self.helper(costs, row+1, 0, total_min_cost + costs[row][1])
            ,self.helper(costs, row+1, 2, total_min_cost + costs[row][1]))
        else:
            return min(self.helper(costs, row+1, 0, total_min_cost + costs[row][2])
            ,self.helper(costs, row+1, 1, total_min_cost + costs[row][2]))
'''
'''
Here we are mutating the matrix
Time Complexity: O(MN) but since colors are fixed => O(3N) or O(N)
Space Complexity: O(1)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs == None or len(costs) == 0:
            return 0
        for i in range(len(costs) - 2, -1,-1):
            costs[i][0] = costs[i][0] + min(costs[i+1][1], costs[i+1][2])
            costs[i][1] = costs[i][1] + min(costs[i+1][0], costs[i+1][2])
            costs[i][2] = costs[i][2] + min(costs[i+1][0], costs[i+1][1])
        return min(costs[0][0], min(costs[0][1], costs[0][2]))
'''
'''
Without mutating the matrix
Time Complexity : O(N)
Space Complexity: O(1)
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs == None or len(costs) == 0:
            return 0
        current_color_red_cost = costs[len(costs)-1][0]
        current_color_green_cost = costs[len(costs)-1][1]
        current_color_blue_cost = costs[len(costs)-1][2]
        for i in range(len(costs) - 2, -1,-1):
            temp_color_red_cost = current_color_red_cost
            temp_color_green_cost = current_color_green_cost
            
            current_color_red_cost = costs[i][0] + min(current_color_green_cost,current_color_blue_cost)
            current_color_green_cost = costs[i][1] + min(temp_color_red_cost, current_color_blue_cost)
            current_color_blue_cost = costs[i][2] + min(temp_color_red_cost, temp_color_green_cost)
        return min(current_color_red_cost, min(current_color_green_cost, current_color_blue_cost))
        
        
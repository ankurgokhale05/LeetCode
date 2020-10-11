'''
Method 1: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        profit = 0
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
                

'''
Method 2: One Pass
Find peaks and valleys in graph and take their difference
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        temp_profit = 0
        buyprice = prices[0]
        
        for i in range(len(prices)):
            sellprice = prices[i]
            if sellprice < buyprice:
                buyprice = sellprice
            else:
                temp_profit = max(temp_profit, sellprice - buyprice)
        return temp_profit
        
    
    
 

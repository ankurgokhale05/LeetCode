# Time Complexity : O(A*C)
# Space Complexity: O(A)
# where A is amount and C is number of different coins.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        if dp[amount] == amount+1:
            return -1
        return dp[amount]
		# return -1 if for a amount, no combination is able to change value from the initial value we had set.
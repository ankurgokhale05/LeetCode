'''
Method 1
Use dynamic programming 
here dp is boolean array of len(s) + 1
dp is an array that contains booleans

dp[i] is True if there is a word in the dictionary that ends at ith index of s AND dp[0] is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

dp[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

dp[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
'''

class Solution:
    def wordBreak(self, s:str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
    



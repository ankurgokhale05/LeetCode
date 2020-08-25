'''
palindrome function finds the longest palindrome in string s expand at
(1) the center m
or
(2) the center between m and m+1.


Complexity Analysis

Time complexity: O(n^2)
where n is the length of the input string.
The algorithm needs to iterate throught the string call palindrome function 2n times. Each time call palindrome function it may go through the whole string, which costs n. So the total time complexity is O(2n*n) = O(n^2)
Space complexity: O(n)
The algorithm needs to maintain two string: sub, and longest, which costs O(n) where n is the length of the input string.
The algorithm needs to maintain three varialbes: m, l, r.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""   
        longest = ""
        for m in range(len(s)):
			# palindrome expands at the center m
            sub = self.palindrome(s, m, m)
            if len(sub) > len(longest):
                longest = sub
			# palindrome expands at the center between m and m + 1
            sub = self.palindrome(s, m, m + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest  
	# palindrome function finds the longest palindrome in string s from center m or center m and m+1.
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1 
        return s[l + 1:r]
        
        
                
            
        
                
    
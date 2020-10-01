# Use a hashmap to store the character frequency and iterate once again to find character whose count is 1 and return the index for that character
#Time Complexity: O(n)
#Space Complexity: O(26) ~ O(1) as 26 characters
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == None or len(s) == 0:
            return -1
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1
            
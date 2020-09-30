'''
Method 1
Use a hashmap to store roman letters with their values. Then we iterate through the string. If there is smaller letter value before bigger letter value subtract from num the smaller letter value. Else add the larger letter value.
The trick is to add the final letter value.


Time Complexity: O(n) where n is length of string.
Space Complexity: O(n) where n is size of dictionary.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num = 0
        for i in range(0, len(s) -1):
            if roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num + roman[s[-1]]
        
                
                
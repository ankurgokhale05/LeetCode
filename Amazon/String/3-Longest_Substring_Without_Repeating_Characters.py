'''
Sliding Window / String
To find longest substring without repeating the characters
We use two pointers both at the start of the string. We use set() of characters to see the characters that we have seen. We move the end pointer and if we see a new character we add it to the set of characters we have seen already. If see a repeating character we remove the character from the set at initial pointer and move further.

Time Complexity: O(n). As b_pointer will iterate through the string.
Space Complexity: O(26) as there are 26 characters but for general scenario depends on size of character set.
'''
class Solution:
    def lengthOfLongestSubstring(self, S: str):
        a_pointer = 0
        b_pointer = 0
        maximum = 0
        characters = set()
        while b_pointer < len(S):
            if S[b_pointer] not in characters:
                characters.add(S[b_pointer])
                b_pointer = b_pointer + 1
                maximum = max(maximum, b_pointer - a_pointer)
            else:
                characters.remove(S[a_pointer])
                a_pointer = a_pointer + 1
        return maximum
# The idea is to use a stack here. Since we have to backtrack once we found a closing bracket for corresponding opening bracket, if found we pop the element from the stack. We continue if stack is not empty return False else return True.
# Time Complexity : O(n)
# Space Complexity : O(n) as we use stack
class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        opening_paren = set(['(', '[','{'])
        bracket_map = {'(':')','[':']', '{':'}'}
        for i in s:
            if i in opening_paren:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
        
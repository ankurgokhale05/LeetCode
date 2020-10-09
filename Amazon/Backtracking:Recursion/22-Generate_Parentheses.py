# As long as we have opening for corresponding closing then it is fine.
# No closing before opening
# We have to use Backtracking
# Total String length == 2* number of opening '(' or 2 * number of closing ')'.

'''
Code Walkthrough
current = ""
output_arr = []
n = 2
maximum = 2 because in main function we set maximum as n
opening = 0
closing  = 0


if (opening < maximum)  as 0 < 2  -> recursive call

    current = '('
    output_arr  = []
    n = 2
    maximum = 2
    opening = 1
    closing = 0
    
    if opening < maximum   as 1 < 2 -> recursive call
    
        current = '(('
        output_arr = []
        n = 2
        maximum = 2
        
        opening = 2
        closing = 0
        
        if opening < maximum   as 2 < 2 -> FALSE
        
    if closing < opening    as 0 < 2 -> recursive call
        current = '()'
        ouput_arr = []
        n = 2
        maximum = 2
        
        opening = 2
        closing. = 1
        
        if opening < max  as 2 < 2 -> False
        
        if closing < opening  as 1 <2
            
            current = "()()"
            output_arr = []
            
            n = 2
            maximum = 2
            
            opening = 2
            closing  = 2
    if closing < opening. as 2< 2 FALSE
    

Time Complexity: O(4^n/n sqrt(n))
Space Complexity: O(4^n/n sqrt(n))
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output_arr = []
        self.backtrack(output_arr, '',0,0,n)
        return output_arr
    
    def backtrack(self, output_arr: List[str] , current_string: str, opening: int, closing: int, maximum: int):
        if len(current_string) == maximum * 2:
            output_arr.append(current_string)
        if opening < maximum:
            self.backtrack(output_arr, current_string + '(', opening + 1, closing, maximum)
        if closing < opening:
            self.backtrack(output_arr, current_string + ')', opening, closing + 1, maximum)
            
        
        
        
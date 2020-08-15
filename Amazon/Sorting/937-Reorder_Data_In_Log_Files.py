#Use Custom Sorting in order to solve this problem
#Total Log Content = N
#Time Complextiy  = O(nlogn)
#Space Complexity = O(n) 
# There can be 4 conditions
'''
1) If first is letter log and second is digit log -> then letter log comes first
2) If first is digit log and second is digit log -> No change
3) If first is letter log and second is letter log -> sort lexicographically
If there is a tie sort them by identifier
4) If first is digit log and second is letter log -> again letter log comes first

'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # divide logs into two parts, one is digit logs, the other is letter logs
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[0])
        #else sort by suffix
        letters.sort(key = lambda x: x.split()[1:])
        #put digit logs after letter logs
        result = letters + digits                                        
        return result         

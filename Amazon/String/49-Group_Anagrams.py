'''
Method: To sort the string and compare each sorted string with the original string if same they are appended to same list
Time Complexity: O(NKlog K) where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog K) time.
Space Complexity: O(NK), the total information content stored in ans
'''

class Solution:
    def groupAnagrams(self, strs: str) -> List[List[str]]:
        dict = {}
        result = []
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in dict:
                dict[sortedword] = [word]
            else:
                dict[sortedword].append(word)
                
        for items in dict.values():
            result.append(items)
        return result
            
            
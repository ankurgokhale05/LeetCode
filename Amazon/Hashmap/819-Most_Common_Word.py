'''
The approach to this problem is that we have to take a hashmap to count the most common word. We need to take a hashset for the banned words. Replace special characters with space, then take lower case and split. Return max count

Time Complexity: O(N)
Space Complexity: O(N)

'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict = {}
        banset = set(banned)
        for ch in  "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        paragraph = paragraph.lower().split()
        
        for word in paragraph:
            if word not in banset:
                if word in dict:
                    dict[word]+=1
                else:
                    dict[word] = 1
        return max(dict,key = dict.get)
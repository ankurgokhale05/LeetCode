
#Method 1: Keep track of last occurence of each character and maintain a last indices array for that. Once end matches with i split at that point and update start pointer.
# Time Complexity: O(N)
# Space Complexity : O(1) as we are taking array for 26 characters
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        output_arr = []
        start = 0
        end = 0
        last_indices = [None] * 26
        l=len(S) # it will be fast if once I calculate it and use multiple times. 
        for i in range(l) :
            last_indices[ord(S[i]) - ord('a')] = i
            
        for i in range(l) :
            end = max(end, last_indices[ord(S[i]) - ord('a')])
            if end == i:
                output_arr.append(end - start + 1)
                start = end + 1
        return output_arr

#Method 1: Use Sorting
# Time Complexity: O(nlogn)
# Space Complexity : O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict ={}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        sorted_dict = sorted(dict, key = lambda word: (-dict[word], word) )
        sorted_dict = sorted_dict[:k]
        return sorted_dict
    
'''
Method 2: Using Heap 
Store the frequencies of all words in a hash table and then find the k frequent using a heap. Here we would have to use a custom comparator for heap because of this reason :-
suppose you have : - (1,"abc") and (1,"cdb") . First element is frequency and second is the actual word. Now according to the question if we have k = 1 answer should be (1,"abc"). According to the defualt heap comparison, the smallest tuple would be (1,"abc") and would be removed from the heap but this should be retained and "cdb" should be popped. So we develop a custom comparator so that if two frequencies are equal keep the largest string at the top so that it is the first to be removed.

Time complexity :- N log k since we never have more than k elements in the heap


'''
from heapq import heappush, heappop, heappushpop

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = defaultdict(int)
        for word in words:
            dict[word] += 1
        
        h = []
        for word, freq in dict.items():
            node = Node(word, freq)
            if len(h) == k:
                heappushpop(h, node)
            else:
                heappush(h, node)
                
        result = []
        while h:
            result.append(heappop(h).word)
        return result[::-1]

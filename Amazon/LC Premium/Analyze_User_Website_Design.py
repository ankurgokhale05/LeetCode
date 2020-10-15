'''
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


'''




class Solution:     
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        '''
        1) The idea is to use min heap to sort the websites visited by each user in ascending order.
        2) then use a dict with users as keys and visited website as values
        3) traverse through each of these lists of websites and create a sequence of 3 for all possible combinations
        4) find the count for each of the sequence
        '''
        queue = []
        heapq.heapify(queue)
        #1) sort data based on timestamp - O(logn) where n = number of users
        for uname,tstamp,wsite in zip(username,timestamp,website):
            heapq.heappush(queue, (tstamp,wsite,uname))
        
        user_dict = defaultdict(list)
        #2) categorize websites based on users - O(n)
        while queue:
            _,web,user = heapq.heappop(queue)
            user_dict[user].append(web)
        
        seq_count_dict = defaultdict(int)
        max_count = 0
        result = tuple()
        
        #3) traverse thriugh all websites to fins sequence of 3 - O(n*k)
        for websites in user_dict.values():
            seq_combinations = combinations(websites,3) #O(k^3) where k is max number of websites visted by a user
            
            for seq in set(seq_combinations): # since we want the count of a sequence visited by most number of users, if a user visits the same sequence multiple times, it is counted as 1
                seq_count_dict[seq] += 1
                
                if seq_count_dict[seq] > max_count:
                    max_count = seq_count_dict[seq]
                    result = seq
                elif seq_count_dict[seq] == max_count: #If the count is same and you find a sequence with a smaller lexographical order
                    if seq < result:
                        result = seq
        return list(result)
        #Time Complexity: O(n*k^3)
        
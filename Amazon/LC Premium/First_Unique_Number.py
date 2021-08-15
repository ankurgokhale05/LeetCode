'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]
Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
'''

'''
Time Complexity:
O(K) for Constructor
O(N) for showFirstUnique
O(1) for Add

'''
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dict_map = {}
        for i in range(len(self.nums)):
            if self.nums[i] not in self.dict_map:
                self.dict_map[self.nums[i]] = 1
            else:
                self.dict_map[self.nums[i]] += 1

    def showFirstUnique(self) -> int:
        for key in self.dict_map.keys():
            if self.dict_map[key] == 1:
                return key
        return -1
        
    def add(self, value: int) -> None:
        self.nums.append(value)
        if value not in self.dict_map:
            self.dict_map[value] = 1
        else:
            self.dict_map[value] += 1

'''
Time Complexity: 
1) For Constructor: O(K); for each K numbers passed into the constructor we're making a call to add(). Each call to add() has a cost of O(1)
2) For Add(): O(1) We are adding in O(1) and removing if number is unique by using ordered dict  or LinkedHashSet it is O(1)
3) For showFirstUnique(): O(1) 

Space Complexity: O(N) 
Each number is stored once in the LinkedHashset. Therefore overall space of O(N)


'''
from collections import OrderedDict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = OrderedDict()
        self._is_unique = {}
        for num in nums:
            # Notice that we're calling the "add" method of FirstUnique; not of the queue. 
            self.add(num)
        
    def showFirstUnique(self) -> int:
        # Check if there is still a value left in the queue. There might be no uniques.
        if self._queue:
            # We don't want to actually *remove* the value.
            # Seeing as OrderedDict has no "get first" method, the way that we can get
            # the first value is to create an iterator, and then get the "next" value
            # from that. Note that this is O(1).
            return next(iter(self._queue))
        return -1
        
    def add(self, value: int) -> None:
        # Case 1: We need to add the number to the queue and mark it as unique. 
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue[value] = None
        # Case 2: We need to mark the value as no longer unique and then 
        # remove it from the queue.
        elif self._is_unique[value]:
            self._is_unique[value] = False
            self._queue.pop(value)
        # Case 3: We don't need to do anything; the number was removed from the queue
        # the second time it occurred.
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
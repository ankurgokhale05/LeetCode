'''
Design a Phone Directory which supports the following operations:

 

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
 

Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
 

Constraints:

1 <= maxNumbers <= 10^4
0 <= number < maxNumbers
The total number of call of the methods is between [0 - 20000]
'''
from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.hash_set = set()
        self.queue = deque()
        for i in range(maxNumbers):
            self.queue.append(i)
            
        
        

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.queue:
            result = self.queue.popleft()
            self.hash_set.add(result)
            return result
        return -1
            

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number not in self.hash_set:
            return True
        return False
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.hash_set:
            self.hash_set.remove(number)
            self.queue.append(number)
        
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
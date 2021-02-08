'''
Meeting Rooms 2
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1


# Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
 
 
 Algorithm

Separate out the start times and the end times in their separate arrays.
Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
Repeat this process until s_ptr processes all of the meetings.
'''


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [] * len(intervals)
        end = [] * len(intervals)
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        
        start.sort()
        end.sort()
        s = 0
        e = 0
        conference_required = 0
        rooms_available = 0
        while s < len(start):
            if start[s] < end[e]:
                if rooms_available == 0:
                    conference_required += 1
                else:
                    rooms_available -= 1
                s += 1
            else:
                rooms_available += 1
                e += 1
        return conference_required
       
'''
Using Min Heap
Time: O(NlogN)
Space: O(N)
'''
import heapq
class Solution:
    def minMeetingRooms(self,intervals: List[List[int]]) -> int:
        if intervals == None:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key = lambda x: x[0])
        heap = []
        heapq.heappush(heap,intervals[0][1])
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)
                
                    
        
        
        
        


'''
Meeting Rooms 1
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
[[0,30],[5,10],[15,20]]

return False

start = [0,5,15] after sorting
end = [10,20,30] after sorting

The idea is to sort start and end time of each interval and just chekc if start of next interval < end of previous interval.

if 5 < 10 then False 

Time Complexity: O(nlogn)
Space Complexity: O(n)

'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = [] * len(intervals)
        end = [] * len(intervals)
        
        
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        print(start)
        print(end)
        start.sort()
        end.sort()
        for i in range(1,len(start)):
            if start[i] < end[i-1]:
                return False
        return True
            
        
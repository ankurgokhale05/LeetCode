# The Idea is to use a Min Heap for all the list and throw every node in the Min Heap. When we throw everything heap all the elements are sorted. Then we pop all elements till length of heap > 0.
# Time Complexity: O(N*Mlog(N*M))
# Space Complexity: O(N*M)
# Here N is Maximum Number of List and M is Maximum number of nodes in list.

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for head in lists:
            while head != None:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = ListNode(0)
        head = dummy
        while len(heap) > 0:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next
        return dummy.next
            
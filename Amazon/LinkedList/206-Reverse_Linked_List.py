# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
We need to keep 3 pointers 1 for next_node, 1 for previous node and 1 for current.
Time Complexity: O(N)
Space Complexity: O(1)

'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        prev = None
        current = head
        next_node = None
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head
            
            
            
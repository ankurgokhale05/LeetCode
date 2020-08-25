# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Iterative solution
Time Complexity: O(M + N)
Space Complexity: O(1)

Here we are dealing with pointers. So we cover base conditions. Then we compare values of l1 and l2 and append the smallest among them.

'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        temp_node = ListNode(0)
        curr_node = temp_node
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
            curr_node.next = l1 or l2
        return temp_node.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1) Set Current and head ListNode as Head
2) Carry variable as 0
3) Iterate through each node of l1 and l2
4) Add value of carry and move the pointer
5) Store the value of carry in current.next
6) Set current = current.next
7) Divide carry by 10
8) Return head.next
Time Complexity: O(max(m,n)+1)
where m is the length of linked list l1, n is the length of linked list l2.
The algorithm needs to iterate at most O(max(m,n)+1) times. "+1" comes from the carry.
Space Complexity:O(max(m,n) + 1)
where m is the length of linked list l1, n is the length of linked list l2.
The algorithm needs to create a new list, and the length will be at most max(m,n)+1
'''     
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        current = head = ListNode(0)
        carry = 0
        while l1 != None or l2!= None or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10
        return head.next
       


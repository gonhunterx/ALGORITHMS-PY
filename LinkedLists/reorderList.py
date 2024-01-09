# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half of list 
        second = slow.next
        slow.next = None 

        # set prev node (will be set to last node we looked at)
        # new head of second half of list 
        prev = slow.next = None
        
        # reverse second half 
        while second:
            # temp var 
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 

        # merge two halfs 
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            # insert 
            first.next = second
            second.next = temp1
            # shift pointers
            first = temp1 
            second = temp2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        start = head
        while start:
            start = start.next
            length += 1
        length //= 2
        start = head
        for i in range(length):
            start = start.next
        nxt = start.next
        start.next = None
        # reverse the list from here prolly hold the temp here
        prev, current = None, nxt
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # merger the two lists
        current = head
        start = prev
        while start:
            nextC = current.next
            nextS = start.next
            current.next = start
            start.next = nextC
            current = nextC
            start = nextS
     # you have two lists head and start, merge them so they alternate

     #make head.next == start then start.next == head.tempnext 
            

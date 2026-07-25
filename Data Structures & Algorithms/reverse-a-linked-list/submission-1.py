# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        return self.recursiveRev(prev, curr)
    def recursiveRev(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return self.recursiveRev(prev, curr)
        else:
            return prev

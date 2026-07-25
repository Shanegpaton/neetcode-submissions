# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        find = length - n
        prev, current = None, head
        if find == 0:
            return head.next
        for i in range(find):
            prev = current
            current = current.next
        prev.next = current.next
        return head
            
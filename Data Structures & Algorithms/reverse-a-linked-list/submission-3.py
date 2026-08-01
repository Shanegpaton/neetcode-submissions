# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            # take the current and point it to the last. make sure to save the pointer to next
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
            



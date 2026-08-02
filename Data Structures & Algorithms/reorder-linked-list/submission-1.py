# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # create two lists reverse one and merge
        list1 = head
        length = 0
        while list1:
            list1 = list1.next
            length += 1 
        mid = length // 2
        list1 = list2 = head
        while mid > 0:
            list2 = list2.next
            mid -= 1
        
        head2 = list2.next
        head1 = head
        list2.next = None
        list2 = head2
        prev = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp
        res = head1
        head2 = prev
        while head1 and head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2

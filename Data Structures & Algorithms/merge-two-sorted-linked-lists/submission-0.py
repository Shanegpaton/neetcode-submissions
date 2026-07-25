# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            lowest = list1
            list1 = list1.next
        else: 
            lowest = list2
            list2 = list2.next
        head = lowest
        while list1 and list2:
            # move the lower pointer to the next lowest number
            if list1.val < list2.val:
                lowest.next = list1
                list1 = list1.next
            else: 
                lowest.next = list2
                list2 = list2.next
            lowest = lowest.next
        if not list1 and list2:
            lowest.next = list2
        if list1 and not list2:
            lowest.next = list1
        return head

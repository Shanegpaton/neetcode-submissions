# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        prev1, curr1 = None, l1
        prev2, curr2 = None, l2 
        while curr1 and curr2:
            total = curr1.val + curr2.val
            if carry:
                total += 1
            curr1.val = total % 10
            if total > 9:
                carry = True
            else:
                carry = False
            prev1, prev2 = curr1, curr2
            curr1, curr2 = curr1.next, curr2.next
            
        if curr2:
            prev1.next = curr2
            prev = prev1
            curr = curr2
        else:
            curr = curr1
            prev = prev1
        while carry and curr:
            if curr.val == 9:
                curr.val = 0
            else:
                curr.val += 1
                carry = False
            prev = curr
            curr = curr.next
            
        if carry:
            curr = ListNode(1)
            prev.next = curr
        return l1
       
        
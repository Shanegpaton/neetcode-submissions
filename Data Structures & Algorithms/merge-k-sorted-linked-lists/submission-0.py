# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # for every linked list check its first value
        # remove the lowest value from the lowest array add it to the return list and repeat
        if len(lists) == 0:
            return None
        dummy = head = ListNode()
        while True:
            lowest = None
            lowestIndex = 0
            for i, node in enumerate(lists):
                if node:
                    lowestIndex = lowestIndex if lowest and lowest.val < node.val else i
                    lowest = lowest if lowest and lowest.val < node.val else node
            if not lowest:
                break
            dummy.next = lowest
            dummy = dummy.next
            lists[lowestIndex] = lists[lowestIndex].next
        return head.next


# while there is a list in lists with value not null

# get every value and check if not null then loop
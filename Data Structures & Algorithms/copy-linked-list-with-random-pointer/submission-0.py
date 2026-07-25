"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a deep copy of the list without the random pointers
        # say we hash the other linkedlist so we have access to the index that the random pointer looks too
        # {object : index}
        # then we hash our linked list and place in the pointers with referance at said index
        # we would hash {index : object} 

        # for every node in the linked list create a deep copy, hash both
        passedMap = {}
        deepMap = {}
        current = head
        index = 0
        dummyHead = Node(0)
        dummy = dummyHead
        while current:
            passedMap[current] = index
            node = Node(current.val)
            deepMap[index] = node
            dummy.next = node
            current = current.next
            dummy = dummy.next
            index += 1
        current = head
        dummy = dummyHead.next
        while current:
            if current.random:
                dummy.random = deepMap[passedMap[current.random]]
            current = current.next
            dummy = dummy.next
        return dummyHead.next

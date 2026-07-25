class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(None, 0)
        self.tail = ListNode(None, 0, None, self.head)
        self.head.next = self.tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node

        return self.cache[key].val        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # handle add and possible delete
            node = ListNode(key, value)
            self.cache[key] = node
            #self.capacity -= 1
            if self.capacity < len(self.cache):
                # handle delete
                deleteKey = self.head.next.key
                print(deleteKey)
                self.cache.pop(deleteKey)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

        else:
            # handle update
            node = self.cache[key]
            node.val = value
            # move to front of list
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        # update the end
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node

class ListNode:
    def __init__(self, key: int, val: int, next: 'ListNode' = None, prev: 'ListNode' = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
# hold a hashset that is {key : node} and a linked list in the order of freq
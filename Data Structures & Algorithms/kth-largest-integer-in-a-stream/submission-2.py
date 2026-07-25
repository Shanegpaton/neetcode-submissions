class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.size:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.size:
            heapq.heappush(self.minHeap, val)
        elif self.minHeap[0] < val:
            heapq.heapreplace(self.minHeap, val)
        return self.minHeap[0]
        
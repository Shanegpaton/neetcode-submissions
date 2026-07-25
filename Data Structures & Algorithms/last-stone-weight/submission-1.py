class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1, stone2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            leftOver = abs(stone1 - stone2)
            heapq.heappush(maxHeap, -leftOver)
        if maxHeap:
            return -maxHeap[0]
        return 0
            
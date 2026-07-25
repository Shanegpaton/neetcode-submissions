class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # look through the list storing in a min heap if they are larger than the smallerst
        # val in the minheap and return the top of the minheap
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                if minHeap[0] < num:
                    heapq.heapreplace(minHeap, num)
        return minHeap[0]
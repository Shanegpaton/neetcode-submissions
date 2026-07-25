class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # rebalance untill len <> 1         
        while (abs(len(self.small) - len(self.large)) > 1 or
          (self.large and -self.small[0] > self.large[0])):
            if len(self.small) > len(self.large):
                temp = heapq.heappop(self.small)
                heapq.heappush(self.large, -temp)
            else: 
                temp = heapq.heappop(self.large)
                heapq.heappush(self.small, -temp)
        
    def findMedian(self) -> float:
        if not self.large:
            return -self.small[0]
        if len(self.small) == len(self.large):
            return ((-self.small[0]) + self.large[0]) / 2
        if len(self.small) > len(self.large):
            return -self.small[0]
        return self.large[0]
    

# small is maxHeap
# large in minHeap
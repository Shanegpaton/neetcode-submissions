class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # converst each point into a distance
        # hold the k smallest distneces and return them
        # store a max heap and if the next value is smaller than the top add and pop
        maxHeap = []
        for point in points:
            distance = math.sqrt((point[1] ** 2) + (point[0] ** 2))
            heapq.heappush(maxHeap, [-distance, point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        array = []    
        for _ in range(len(maxHeap)):
            array.append(heapq.heappop(maxHeap)[1])
        return array     
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        buckets = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            buckets[count - 1].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for bucket in buckets[i]:
                    if len(res) == k:
                        return res
                    res.append(bucket)
        return res
            
            
                

            

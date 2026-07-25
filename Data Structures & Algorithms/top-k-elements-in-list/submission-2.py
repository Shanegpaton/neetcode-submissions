class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for key, value in counts.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for numbers in freq[i]:
                res.append(numbers)
            if len(res) == k:
                return res
        
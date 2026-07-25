class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create an array to store the count of each letter form a-z
        # loop through the array incementing the count in the array and 
        # chech if the new index holds a greater value than the highest number 
        # of duplicates if it does update it. return heighest
        freqs = [0] * 26
        maxFreq = 0
        for task in tasks:
            freqs[ord(task) - ord('A')] += 1
            maxFreq = max(maxFreq, freqs[ord(task) - ord('A')])
        maxCount = 0
        for freq in freqs:
            if freq == maxFreq:
                maxCount += 1
        # repeat =    
        repeat = (maxFreq - 1) * (n + 1) + maxCount
        return max(repeat, len(tasks))

        # if 5 repeats and 2 cycles min = 10
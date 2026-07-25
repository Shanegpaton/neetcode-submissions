class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the lowest number of bph you could have and still eat all bannanas
        # hours and the number of pile. how fast to eat all of the piles within the hours 
        # the fastest possible needed time would be the largest pile. try each pile using the sorted guess
        # until you find the lowest number
        maxPile = 0
        for size in piles:
            maxPile = max(size, maxPile)
        l, r = 1, maxPile 
        while l < r:
            middle = (r + l) // 2
            if self.check(middle, piles, h):
                r = middle
            else: 
                l = middle + 1 
        return l

    def check(self, middle: int, piles: List[int], h: int) -> bool:
        # true means all bannans can be eaten in the time
        time = 0
        for pile in piles:
            time += math.ceil(pile / middle)
        return time <= h

# search that finds the last true value
# while l < r
# if check is true move the left pointer to the spot after
# if the check is false move the right pointer to the spot

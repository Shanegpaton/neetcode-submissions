class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        rCount = lCount = 0
        currentPair = []
        self.createPairs(n, rCount, lCount, currentPair, pairs)
        return pairs


 # create up to n right para
    # use up to n left para
    # if the total length is 2 n add it to the array and return
    # if the count of ( is < than the count of ) stop
    
    def createPairs(self, n: int, rCount: int, lCount: int, currentPair: [], pairs: []) -> None:
        if (rCount + lCount == 2 * n):
            pairs.append("".join(currentPair))
            return
        if (lCount > rCount):
            currentPair.append(")")
            self.createPairs(n, rCount + 1, lCount, currentPair, pairs)
            currentPair.pop()
        if (lCount < n):
            currentPair.append("(")
            self.createPairs(n, rCount, lCount + 1, currentPair, pairs)
            currentPair.pop()
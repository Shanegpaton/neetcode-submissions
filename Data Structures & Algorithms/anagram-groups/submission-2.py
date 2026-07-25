class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return dic key = bag of letters -> value = each word
        r = {}
        # convert each str to a bag of letters and check
        for s in strs:
            bag = [0 for i in range(26)]
            for c in s:
                bag[ord(c) - ord('a')] += 1
            tup = tuple(bag)
            if tup in r:
                r[tup].append(s)
            else:
                r[tup] = [s]
        return [v for v in r.values()]
            
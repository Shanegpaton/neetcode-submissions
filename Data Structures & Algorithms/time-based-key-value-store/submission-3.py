class TimeMap:

    def __init__(self):
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.pairs:
            self.pairs[key] = [[timestamp, value]]
        else: 
            self.pairs[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pairs:
            return ""
        array = self.pairs[key]
        l, r = 0, len(array)
        while l < r:
            middle = (l + r) // 2
            if array[middle][0] == timestamp:
                return array[middle][1]
            if array[middle][0] < timestamp:
                l = middle + 1
            else: 
                r = middle
        return array[l - 1][1] if array[l - 1][0] <= timestamp else "" 



# i need to hold a key value paired at a time. 
# [time key vale]


# when i look up a name i get back an array of timestamp value pairs
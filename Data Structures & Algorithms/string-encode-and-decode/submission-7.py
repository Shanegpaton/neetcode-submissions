class Solution:

    def encode(self, strs: List[str]) -> str:
        # count|len|len|strs 3|5|6|8|
        if strs == [""]:
            return ""
        res = f"{len(strs)}|"
        for s in strs:
            res += str(len(s)) + "|"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        res = []
        keys = []
        counter = 0
        for i in range(len(s)):
            counter = i
            if s[i] == '|':
                break
        size = int(s[0:counter])
        print(f"{counter} + {size}")
        # loop through string until you find size |
        temp = ""
        start = 0
        for i in range(counter + 1, len(s)):
            if len(keys) == size:
                start = i
                break
            if s[i] == '|':
                keys.append(int(temp))
                temp = ""
            else:
                temp += s[i]
        total = 0
        for i in range(size):
            si = start + total
            res.append(s[si: si + keys[i]])
            total += keys[i]
        return res


        
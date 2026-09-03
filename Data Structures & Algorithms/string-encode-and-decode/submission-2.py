class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for e in strs:
            res += str(len(e)) + "#" + "".join(e)
        
        return res

    def decode(self, s: str) -> List[str]:
        res, p = [], 0

        while p < len(s):
            j = p
            while s[j] != "#":
                j += 1
            length = int(s[p:j]) # how many char. we have to read after j
            res.append(s[j+1:j+1+length])
            p = j+1+length
        return res


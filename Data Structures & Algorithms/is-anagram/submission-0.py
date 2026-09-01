class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        if sorted_s == sorted_t:
            res = True
        return res
        


        
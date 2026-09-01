class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = True
        res = list(dict.fromkeys(nums))
        print(nums)
        print(res)
        if len(res) == len(nums):
            r = False
        return r
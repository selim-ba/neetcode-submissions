class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
       #Version 1
        r = True
        res = list(dict.fromkeys(nums))
        print(nums)
        print(res)
        if len(res) == len(nums):
            r = False
        return r
        """

        # Version 2 - HashSet
        hashset = set()
        #print(hashset)
        for n in nums:
            if n in hashset:
                #print(n,hashset)
                return True
            hashset.add(n)
            #print(n,hashset)
        return False
        
                
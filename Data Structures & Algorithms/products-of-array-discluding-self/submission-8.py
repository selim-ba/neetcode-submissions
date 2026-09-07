class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Version 1 - 29/51 test cases
        #res = []
        #for i,n in enumerate(nums):
        #    temp = nums[:i] + nums[i+1:]

        #    product = 1
        #    for t in temp:
        #        product *= t
                
        #    res.append(product)
        #return res

        # Version 2 - 
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
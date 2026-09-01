class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        R = []
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        R.append(i)
                        R.append(j)
        R = list(dict.fromkeys(R))
        return R

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        # Version 1 (65ms)
        R = []
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    R.append(i)
                    R.append(j)
        return R
        """

        """
        # Version 2 (85ms)
        R = []
        i = 0
        j = 1
        while (nums[i] + nums[j] != target) & (j <= len(nums)):
            j += 1
            if j == len(nums):
                i += 1
                j = i + 1
        R.append(i)
        R.append(j)
        return R
        """

        # Version 3 - HashMap - 30ms
        prevMap =  {} # val : index
        for i,n in enumerate(nums):
            #print(i,n)
            diff = target - n
            if diff in prevMap:
                print(diff,prevMap[diff])
                print(prevMap)
                return [prevMap[diff],i]
            prevMap[n] = i
        return

        

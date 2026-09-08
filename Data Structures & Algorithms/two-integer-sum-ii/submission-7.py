class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = -1
        p_1 = 0
        p_2 = 0

        p_1 = numbers[i]
        p_2 = numbers[j]
        while (p_1 + p_2 != target) and (i < (len(numbers)+j)):
            if p_1 + p_2 > target:
                j -= 1
                p_2 = numbers[j]
            if p_1 + p_2 < target:
                i += 1
                p_1 = numbers[i]
        return [i+1,len(numbers)+j+1]

        
        
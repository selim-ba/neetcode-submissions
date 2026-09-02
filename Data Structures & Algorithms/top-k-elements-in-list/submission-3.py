class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Version 1 - Sorting a dict based on most frequent values
        """
        Map = {value: 0 for value in nums}
        for i in nums:
            if i in Map.keys():
                Map[i] += 1
                #print(Map)

        most_k = sorted(Map, key=Map.get, reverse=True)[:k]
        return most_k
        """

        # Version 2 - Bucker Sort : time and psace cplx of O(n)
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num,0) # 1 + num or 1 + 0 if num doesnt exist in count

        for num, cnt in count.items():
            freq[cnt].append(num)
            #print(num,cnt,freq)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) ==k:
                    return res








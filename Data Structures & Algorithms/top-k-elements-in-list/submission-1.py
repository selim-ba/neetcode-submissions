class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {value: 0 for value in nums}
        for i in nums:
            if i in Map.keys():
                Map[i] += 1
                #print(Map)

        #print(Map)
        #print(sorted(Map))
        #print(sorted(Map,key=Map.get,reverse=True))
        #most_k = sorted(Map, key=Map.get)[-k:]
        most_k = sorted(Map, key=Map.get, reverse=True)[:k]
        return most_k

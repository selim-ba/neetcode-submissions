class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Version 1 (works only on test cases)
        """
        Map = dict()
        for i,n in enumerate(strs):
            if ''.join(sorted(n)) in Map:
                Map[''.join(sorted(strs[i]))].append(''.join(strs[i]))
            else:
                Map[''.join(sorted(strs[i]))] = []
                Map[''.join(sorted(strs[i]))].append(''.join(strs[i]))
        print(Map.values())
        res = list(Map.values())
        return res
        """

        # Version 2
        Map = {}
        for n in strs:
            key = ''.join(sorted(n))

            if key in Map:
                Map[key].append(n)
                #print(n,key,Map)
            else:
                Map[key] = [n]
                #print(n,key,Map)

        return list(Map.values())

                




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # O(n * k log k)
        for index, str in enumerate(strs):
            hash = self.getStringHash(str)
            if hash not in groups:
                groups[hash] = []
            groups[hash].append(index)
        
        return [[strs[i] for i in arr] for arr in groups.values()]

    def getStringHash(self, s: str) -> str:
        # O(k log k) + O(k)
        return "".join(sorted(s))

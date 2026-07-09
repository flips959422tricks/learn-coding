class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # O(n * k log k)
        for str in strs:
            hash = self.getStringHash(str)
            if hash not in groups:
                groups[hash] = []
            groups[hash].append(str)
        
        return list(groups.values())

    def getStringHash(self, s: str) -> str:
        # O(k log k) + O(k)
        return "".join(sorted(s))

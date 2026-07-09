class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # O(n * k)
        for s in strs:
            key = self.get_count_key(s)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())

    # O(k)
    def get_count_key(self, s: str) -> tuple[int, ...]:
        counts = [0] * 26
        for ch in s:
            index = ord(ch) - ord("a")
            counts[index] += 1
        return tuple(counts)

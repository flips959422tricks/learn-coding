class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # easy early exit
        if len(s) != len(t):
            return False

        counts = {}
        
        # increase count per char
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        # decrease count per char
        for char in t:
            counts[char] = counts.get(char, 0) - 1
            # early exit condition
            if counts[char] < 0:
                return False
        
        if sum(counts.values()) != 0:
            return False

        return True

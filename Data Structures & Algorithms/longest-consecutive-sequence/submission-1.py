class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        numset = set(nums)
        
        # max size var
        max_size = 0

        # loop over the set
        for n in numset:
            # if an element is an in-betweener, skip it
            # if it is a series starter, start counting from it and incrementing max size
            if n-1 not in numset:
                i = 0
                gap_found = False
                while i < len(numset) and gap_found == False:
                    if n+i in numset:
                        max_size = max(max_size, i+1)
                    else:
                        gap_found = True
                    i = i + 1

        return max_size

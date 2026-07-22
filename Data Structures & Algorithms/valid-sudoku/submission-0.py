import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        buckets = {}

        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el != ".":
                    # keys
                    r_key = ("r",i,el)
                    c_key = ("c",j,el)
                    s_key = ("s",math.floor(i/3),math.floor(j/3),el)

                    # check
                    if r_key in buckets or c_key in buckets or s_key in buckets:
                        return False
                    
                    # increment
                    buckets[r_key] = 1
                    buckets[c_key] = 1
                    buckets[s_key] = 1
        
        return True
                    
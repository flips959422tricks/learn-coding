import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        buckets = set()

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
                    buckets.add(r_key)
                    buckets.add(c_key)
                    buckets.add(s_key)
        
        return True
                    
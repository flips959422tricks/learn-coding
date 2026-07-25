class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums.copy()
        sorted_nums.sort()

        triplets = set()

        for i in range(len(sorted_nums)-2):
            j = i + 1
            k = len(sorted_nums) - 1
            jk_sum = -1 * sorted_nums[i]

            while j < k:
                if sorted_nums[j] + sorted_nums[k] < jk_sum:
                    j = j + 1
                elif sorted_nums[j] + sorted_nums[k] > jk_sum:
                    k = k - 1
                else:
                    arr = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    arr.sort()
                    triplets.add(tuple(arr))

                    # repeated adjacent numbers check
                    if sorted_nums[j] == sorted_nums[j+1]:
                        j = j + 1
                    elif sorted_nums[k] == sorted_nums[k-1]:
                        k = k - 1
                    else:
                        j = j + 1
        
        return list(triplets)

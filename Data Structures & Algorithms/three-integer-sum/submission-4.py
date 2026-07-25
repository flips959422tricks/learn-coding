class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums.copy()
        sorted_nums.sort()

        triplets = []

        i = 0
        while i < len(sorted_nums) - 2:
            
            # duplicate adjacent skip
            if i != 0 and sorted_nums[i] == sorted_nums[i-1]:
                i = i + 1
                continue

            # vars
            j = i + 1
            k = len(sorted_nums) - 1
            jk_target = -1 * sorted_nums[i]

            # inner loop
            while j < k:
                # duplicate adjacent skip
                if j != i+1 and sorted_nums[j] == sorted_nums[j-1]:
                    j = j + 1
                    continue
                elif k != len(sorted_nums)-1 and sorted_nums[k] == sorted_nums[k+1]:
                    k = k - 1
                    continue

                jk_sum = sorted_nums[j] + sorted_nums[k]

                if jk_sum < jk_target:
                    j = j + 1
                elif jk_sum > jk_target:
                    k = k - 1
                else:
                    arr = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    triplets.append(arr)
                    j = j + 1
                    k = k - 1

            i = i + 1
        
        return list(triplets)

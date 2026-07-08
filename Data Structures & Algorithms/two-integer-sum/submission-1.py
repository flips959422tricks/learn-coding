class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O (n^2)
        for i_index, i in enumerate(nums):
            for j_index in range(i_index + 1, len(nums)):
                j = nums[j_index]
                if i + j == target:
                    return [i_index, j_index]




        
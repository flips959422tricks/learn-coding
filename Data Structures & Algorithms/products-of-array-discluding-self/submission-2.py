class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1]*len(nums)
        for i, n in enumerate(nums):
            for j in range(len(product_array)):
                if i != j:
                    product_array[j] = product_array[j] * n
        return product_array
        
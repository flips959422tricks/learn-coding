class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [1]*len(nums)
        for n in nums:
            for i in range(len(product_array)):
                if n != i:
                    product_array[i] = product_array[i] * n
        return product_array
        
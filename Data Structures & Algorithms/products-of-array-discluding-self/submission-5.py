class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product_array = [1] * size
        
        # left pass
        for i in range(size):
            if i != 0:
                product_array[i] = nums[i-1] * product_array[i-1]
        
        # right pass
        right_product_value = 1
        for i in range(size):
            r_index = size - 1 - i
            product_array[r_index] = product_array[r_index] * right_product_value
            right_product_value = right_product_value * nums[r_index]

        return product_array
        
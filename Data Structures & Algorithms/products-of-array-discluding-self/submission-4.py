class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_product_array = [1] * size
        right_product_array = [1] * size
        for i in range(size):
            if i != 0:
                left_product_array[i] = nums[i-1] * left_product_array[i-1]
                
                r_index = size - 1 - i
                right_product_array[r_index] = nums[r_index + 1] * right_product_array[r_index + 1]
        
        product_array = [1] * size
        for i in range(size):
            product_array[i] = left_product_array[i] * right_product_array[i]

        return product_array
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_array = [0] * len(prices)
        max_from_right = 0
        for i in range(len(prices)):
            r_ind = len(prices) - 1 - i
            max_from_right = max(prices[r_ind], max_from_right)
            max_array[r_ind] = max_from_right
        
        max_diff = 0
        for i in range(len(prices)):
            max_diff = max(max_diff, max_array[i]-prices[i])
        
        return max_diff


        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_max_from_right = 0

        for i in range(len(prices)):
            right_index = len(prices) - 1 - i
            current_max_from_right = max(current_max_from_right, prices[right_index])
            max_profit = max(max_profit, current_max_from_right - prices[right_index])
        
        return max_profit
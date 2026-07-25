class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            lh = heights[left]
            rh = heights[right]

            area = min(lh, rh) * (right - left)
            max_area = max(max_area, area)

            if lh < rh:
                left = left + 1
            elif rh < lh:
                right = right - 1
            else:
                left = left + 1
                right = right - 1
        
        return max_area
        
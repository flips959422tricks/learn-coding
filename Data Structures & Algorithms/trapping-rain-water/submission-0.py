class Solution:
    def trap(self, height: List[int]) -> int:
        max_from_left = 0
        running_max_from_left = []
        for i in range(len(height)):
            max_from_left = max(max_from_left,height[i])
            running_max_from_left.append(max_from_left)

        max_from_right = 0
        running_max_from_right = []
        for i in range(len(height)-1, -1, -1):
            max_from_right = max(max_from_right,height[i])
            running_max_from_right.insert(0, max_from_right)
        
        total_water = 0
        for i in range(len(height)):
            current_water_stack = max(0, min(running_max_from_left[i], running_max_from_right[i]) - height[i])
            total_water = total_water + current_water_stack
        
        return total_water

        
        
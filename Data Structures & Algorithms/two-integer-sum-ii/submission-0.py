class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0

        while i < len(numbers) - 1:

            j = len(numbers) - 1
            # note: as j decreases, the number it points to gets smaller

            while j > i:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

                if numbers[i] + numbers[j] < target:
                    break
                
                j = j - 1
            
            i = i + 1
        
        return [0, len(numbers) - 1]
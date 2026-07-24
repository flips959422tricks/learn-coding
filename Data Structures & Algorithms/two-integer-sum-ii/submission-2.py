class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0

        while i < len(numbers) - 1:
            # start at end
            j = len(numbers) - 1

            # knowingly using nonsensical a value that won't exit the while loop on the first check
            prev_j = j + 1

            while j != prev_j:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                elif numbers[i] + numbers[j] > target:
                    # move j towards i
                    new_j = (i + j) // 2
                    prev_j = j
                    j = new_j
                else:
                    # move j towards prev_j
                    new_j = (prev_j + j) // 2
                    prev_j = j
                    j = new_j
            
            i = i + 1

        return [0, len(numbers) - 1]
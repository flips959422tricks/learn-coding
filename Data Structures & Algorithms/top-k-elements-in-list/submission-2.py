class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        index_wise_nums = [[] for _ in nums]
        for item in num_counts.items():
            index_wise_nums[item[1] - 1].append(item[0])

        result = []
        for i in range(len(nums)):
            result.extend(index_wise_nums[len(nums) - i - 1])
            if len(result) >= k:
                return result[:k]

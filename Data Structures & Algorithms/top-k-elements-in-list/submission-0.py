class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        sorted_list = sorted(num_counts.items(), key=lambda arr: -arr[1])
        top_list = [arr[0] for arr in sorted_list[:k]]
        
        return list(top_list)

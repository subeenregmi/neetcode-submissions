from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
            
        return sorted(list(frequencies), key=lambda num: frequencies[num], reverse=True)[:k]
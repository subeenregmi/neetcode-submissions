class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()

        for i in range(len(nums)):
            num_index[nums[i]] = i
        
        for j, num in enumerate(nums):
            if target - num in num_index and j != num_index[target - num]:
                return [min(num_index[target - num], j), max(num_index[target - num], j)]
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCount = Counter(nums)

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in numsCount:
                continue

            for j in range(i+1, len(nums)):
                if nums[j] == rem:
                    return [i, j]
         
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_index = -1
        for i, n in enumerate(nums):
            if n == 0:
                if zero_index == -1:
                    zero_index = i
                else:
                    prod = 0
            else:
                prod *= n
        
        print(prod, zero_index)

        if prod == 0:
            return [0] * len(nums)

        if zero_index != -1:
            temp = [0] * len(nums)
            temp[zero_index] = prod
            return temp    

        for i in range(len(nums)):
            nums[i] = int(prod / nums[i])

        return nums
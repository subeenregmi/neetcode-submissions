class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_seq = 0
        for n in nums:
            seq = 0
            if n-1 not in s:
                x = n
                seq += 1
                while x+1 in s:
                    seq += 1
                    x += 1
            else:
                continue
            if seq > longest_seq:
                longest_seq = seq
        return longest_seq
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)
        longest_chain = 0
        seen = set()

        for n in nums:
            current_chain = 1

            if n in seen:
                continue

            seen.add(n)
            
            while n + 1 in items:
                current_chain += 1
                n += 1
                seen.add(n)

            longest_chain = max(current_chain, longest_chain)

        return longest_chain
                

                

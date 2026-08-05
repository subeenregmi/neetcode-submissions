class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = dict()

        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                s_chars[char] += 1 

        for char in t:
            if char not in s_chars:
                return False
            else:
                s_chars[char] -= 1 
            
        for char in s_chars:
            if s_chars[char] != 0:
                return False

        return True
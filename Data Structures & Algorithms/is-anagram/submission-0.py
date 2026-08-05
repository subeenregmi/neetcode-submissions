from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = Counter()
        t_chars = Counter()
        
        for c in s:
            s_chars[c] += 1

        for c in t:
            t_chars[c] += 1

        for k in s_chars.keys():
            if s_chars[k] != t_chars[k]:
                return False

        return True
        
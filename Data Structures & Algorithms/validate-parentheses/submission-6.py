class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            c = s[i]
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                p = stack.pop()

                if (p == '{' and c == "}") or (p == '[' and c == ']') or (p == '(' and c == ')'):
                    continue
                else:
                    return False
        
        if len(stack) != 0:
            return False

        return True
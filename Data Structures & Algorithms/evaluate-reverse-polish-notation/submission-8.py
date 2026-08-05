import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(t, stack)
            if t[0] == "-" and t[1:].isnumeric():
                stack.append(int(t[1:])*-1)
            else:
                if t.isnumeric():
                    stack.append(int(t))
                else:
                    if t == "+":
                        stack.append(stack.pop() + stack.pop())
                    if t == "-":
                        v = stack.pop()
                        stack.append(stack.pop() - v)
                    if t == "*":
                        stack.append(stack.pop() * stack.pop())
                    if t == "/":
                        v = stack.pop()
                        stack.append(int(stack.pop() / v))

        return stack[-1]
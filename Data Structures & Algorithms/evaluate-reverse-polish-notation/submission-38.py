import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for t in tokens:
            if t not in operators:
                stack.append(int(t)) 
                continue

            op1 = stack.pop()
            op2 = stack.pop()

            if t == '+':
                stack.append(op1 + op2)
                continue

            if t == '-':
                stack.append(op2 - op1)
                continue

            if t == '*':
                stack.append(op1 * op2)
                continue

            if t == '/':
                stack.append(math.trunc(op2 / op1))
                continue
        
        return int(stack.pop())

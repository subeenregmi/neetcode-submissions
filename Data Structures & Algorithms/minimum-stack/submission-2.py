import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.head = -1
        self.Min = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.head += 1
        if val <= self.Min[-1]:
            self.Min.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        self.head -= 1
        if v <= self.Min[-1]:
            self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]
        

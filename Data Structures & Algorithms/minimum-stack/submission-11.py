class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, val: int) -> None:
        self.data.append(val)

        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)
        
    def pop(self) -> None:
        item = self.data.pop()
        if item == self.mins[-1]:
            self.mins.pop()
            
        return item

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        

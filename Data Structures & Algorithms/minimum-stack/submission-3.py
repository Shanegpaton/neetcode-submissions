class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.history) > 0):
            smallest = min(self.history[len(self.history) - 1], val)
        else: 
            smallest = val
        self.history.append(smallest)

    def pop(self) -> None:
        del self.stack[len(self.stack) - 1]
        del self.history[len(self.history) - 1]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.history[-1]

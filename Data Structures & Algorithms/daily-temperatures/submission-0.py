class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # find how many days until the next warmer day and return it in an araay
        # use a monotinic stack to hold the next day
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # while the stacks top value is less than current temp pop it and add 
            # the current day - day in stack to the result at day in stack
            while (len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]):
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            # add it to the stack if the stack is empty or the top is higher
            stack.append(i)
        return result

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find the largerest area of the heights
        # the area is found by the lowest point accross the span of rectangles and the size 
        # add the highest values and hold them until there is a lower value
        # hold all the values in a stack pop all values higher than the current value
        # check the area of the stack when popping?
        # the number of values popped is the width. 
        # the lowest value popped is the hight find max of that and current max
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            # check if it is larger than top
            lastPopped = None
            popped = False
            while (stack and heights[i] < heights[stack[-1]] ):
                width = i - stack[-1]
                maxArea = max(heights[stack[-1]] * width, maxArea)
                heights[stack[-1]] = heights[i]
                lastPopped = stack[-1]
                popped = True
                stack.pop()
            # add to stack
            if not popped:
                stack.append(i)
            else:  
                stack.append(lastPopped)
                stack.append(i)
        while (len(stack) > 1):
            width = (stack[-1] - stack[-2] - 1) + len(heights) - stack[-1]
            maxArea = max(heights[stack[-1]] * width, maxArea)
            stack.pop()
        maxArea = max(heights[stack[0]] * (len(heights) - stack[0]), maxArea)
        return maxArea


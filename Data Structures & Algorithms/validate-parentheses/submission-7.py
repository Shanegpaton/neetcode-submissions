class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1] == "{" and char == "}":
                stack.pop()
            elif stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False
            
            
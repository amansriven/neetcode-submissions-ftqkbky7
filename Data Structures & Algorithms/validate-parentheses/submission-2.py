from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if c == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        if stack:
            return False
        return True

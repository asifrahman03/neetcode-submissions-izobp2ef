class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not bool(stack) and c != None:
                return False
            elif stack[-1] == '(' and c != ')':
                return False
            elif stack[-1] == '[' and c != ']':
                return False
            elif stack[-1] == '{' and c != '}':
                return False
            elif stack[-1] == '(' and c == ')':
                stack.pop()
            elif stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack[-1] == '{' and c == '}':
                stack.pop()
        return not bool(stack)
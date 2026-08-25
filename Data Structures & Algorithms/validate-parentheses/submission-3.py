class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []
        for l in s:
            if len(stack) == 0: 
                stack.append(l)
                continue

            if l == ')' and stack[len(stack) - 1] == '(':
                stack.pop()
                continue
            if l == '}' and stack[len(stack) - 1] == '{':
                stack.pop()
                continue
            if l == ']' and stack[len(stack) - 1] == '[':
                stack.pop()
                continue
            stack.append(l)

        if len(stack) == 0: return True
        return False
        
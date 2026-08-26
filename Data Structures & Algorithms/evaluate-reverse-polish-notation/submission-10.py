class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n not in ("+","-","*","/"):
                stack.append(int(n))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                res = self.math_op(val2, val1, n)
                stack.append(res)
        return int(stack[0])


    def math_op(self, val1, val2, op) -> int:
        if op == "+":
            return val1 + val2
        elif op == "-":
            return val1 - val2
        elif op == "*":
            return val1 * val2
        else:
            return int(val1 / val2)
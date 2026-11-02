import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda x, y: int(x / y)}

        for char in tokens:
            if char in '+-*/':
                a, b = stack.pop(), stack.pop()
                result = operations[char](b, a)
                stack.append(result)
            else:
                stack.append(int(char))

        return stack.pop()
            
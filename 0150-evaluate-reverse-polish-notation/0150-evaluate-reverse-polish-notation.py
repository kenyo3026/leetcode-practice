class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:

            if len(stack) >= 2:
                if token == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a) + int(b))
                    continue

                elif token == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a) - int(b))
                    continue

                elif token == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a) * int(b))
                    continue

                elif token == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a) / int(b))
                    continue

            stack.append(token)

        return int(stack[-1])
class Solution:
    def reverseParentheses(self, s: str) -> str:
        op, cl = '(', ')'
        stack = [[]]

        for char in s:
            if char == op:
                stack.append([])
            elif char == cl:
                top = stack.pop()
                stack[-1].extend(reversed(top))
            else:
                stack[-1].extend(char)

        return ''.join(stack[-1])

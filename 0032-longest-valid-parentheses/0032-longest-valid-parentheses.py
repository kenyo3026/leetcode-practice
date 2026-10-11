class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    if stack:
                        max_length = max(max_length, i-stack[-1])
                    else:
                        max_length = max(max_length, i-start+1)
                else:
                    start = i + 1
        return max_length
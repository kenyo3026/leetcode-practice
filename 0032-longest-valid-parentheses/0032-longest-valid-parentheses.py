class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)

        stack = []
        i, max_valid = 0, 0
        for j in range(n):

            if s[j] == "(":
                stack.append(j)

            else:

                if stack:
                    stack.pop()

                    if stack:
                        max_valid = max(max_valid, j - stack[-1])

                    else:
                        max_valid = max(max_valid, j - i + 1)

                else:
                    i = j + 1

        return max_valid
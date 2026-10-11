class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_valid = 0

        op_so_far, cl_so_far = 0, 0
        for char in s:
            if char == '(':
                op_so_far += 1
            else:
                cl_so_far += 1

            if op_so_far == cl_so_far:
                max_valid = max(max_valid, op_so_far * 2)

            if op_so_far < cl_so_far:
                op_so_far, cl_so_far = 0, 0

        op_so_far, cl_so_far = 0, 0
        for char in s[::-1]:
            if char == '(':
                op_so_far += 1
            else:
                cl_so_far += 1

            if op_so_far == cl_so_far:
                max_valid = max(max_valid, op_so_far * 2)

            if op_so_far > cl_so_far:
                op_so_far, cl_so_far = 0, 0

        return max_valid
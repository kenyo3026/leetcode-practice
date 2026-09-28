class Solution:
    def maxDepth(self, s: str) -> int:
        op, cl = '(', ')'
        depth, max_depth = 0, 0

        for char in s:
            if char == op:
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == cl:
                depth -= 1

        return max_depth
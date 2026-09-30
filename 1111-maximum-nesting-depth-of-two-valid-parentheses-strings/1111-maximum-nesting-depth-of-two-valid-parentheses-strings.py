class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth, ans = 1, []

        for char in seq:
            if char == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1
        return ans
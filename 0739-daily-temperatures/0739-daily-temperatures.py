class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, stack = [0] * n, []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                tmp = stack.pop()
                ans[tmp] = i - tmp

            stack.append(i)

        return ans

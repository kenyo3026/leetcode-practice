class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (limit * 2 + 2)

        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            x, y = min(a, b), max(a, b)

            # 全部先 +2
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # 一次修改區間
            diff[x+1] -= 1
            diff[y + limit + 1] += 1

            # 不用修改
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        ans = float('inf')
        cur = 0

        for t in range(2, 2 * limit + 1):
            cur += diff[t]
            ans = min(ans, cur)

        return ans
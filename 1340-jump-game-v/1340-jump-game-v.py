class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n

        # sort indices by height ascending so dp[j] is ready before computing dp[i] 
        # (i depends on shorter neighbors)
        indices = sorted(range(n), key=lambda i: arr[i])

        for i in indices:

            for j in range(i+1, min(n, i + d + 1)):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                else:
                    break

            for j in range(i-1, max(-1, i - d - 1), -1):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                else:
                    break

        return max(dp)
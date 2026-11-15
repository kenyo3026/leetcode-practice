class Solution:
    MOD = 10 ** 9 + 7

    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        odd = [0] * n
        even = [0] * n

        if arr[0] % 2:
            odd[0] = 1
        else:
            even[0] = 1

        for i in range(1, n):
            if arr[i] % 2:
                odd[i] = even[i-1] + 1
                even[i] = odd[i-1]
            else:
                odd[i] = odd[i-1]
                even[i] = even[i-1] + 1

        return sum(odd) % self.MOD
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_len, high_len = str(low).__len__(), str(high).__len__()
        pool = "123456789"
        pool_len = pool.__len__()
        combinations = []

        for j in range(low_len, high_len + 1):
            for i in range(pool_len - j + 1):
                comb = int(pool[i:i+j])
                if comb < low:
                    continue
                elif comb > high:
                    break
                combinations.append(comb)

        return combinations
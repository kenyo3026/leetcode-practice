class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = Counter(f for f, _ in items)
        mx = max(freq)

        # mult[f] = number of items whose factor is a multiple of f (including f itself)
        mult = {}
        for f in freq:
            total = 0
            for k in range(f, mx + 1, f):
                total += freq.get(k, 0)
            mult[f] = total

        m = min(p for _, p in items)
        ans = 0
        remain = budget

        for f, p in sorted(items, key=lambda x: x[1]):
            if p > 2 * m or p > remain:
                break
            c = mult[f] - 1          # exclude the item itself
            t = min(c, remain // p)
            ans += 2 * t
            remain -= t * p

        ans += remain // m
        return ans
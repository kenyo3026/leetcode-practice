import heapq

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        LOG = n.bit_length() + 1
        self.mx = [nums[:] for _ in range(LOG)]
        self.mn = [nums[:] for _ in range(LOG)]
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                self.mx[j][i] = max(self.mx[j-1][i], self.mx[j-1][i + (1 << (j-1))])
                self.mn[j][i] = min(self.mn[j-1][i], self.mn[j-1][i + (1 << (j-1))])

    def query(self, l, r):
        if l > r:
            return 0
        k = (r - l + 1).bit_length() - 1
        mx = max(self.mx[k][l], self.mx[k][r - (1 << k) + 1])
        mn = min(self.mn[k][l], self.mn[k][r - (1 << k) + 1])
        return mx - mn

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        st = SparseTable(nums)

        # heap: (-val, l, r_lo, r_hi)
        # meaning: subarray starting at l, with r chosen as r_hi (best in [r_lo, r_hi])
        # after picking (l, r_hi), split r range into [r_lo, r_hi-1]
        # and also push (l+1, r_hi, r_hi, r_hi) ... but this misses combos
        
        # Correct approach: (-val, l_lo, l_hi, r_lo, r_hi)
        # represents the best subarray where l in [l_lo, l_hi], r in [r_lo, r_hi]
        # always evaluated at corners: we pick the globally best subarray value
        # Since value is monotone (larger range >= smaller range),
        # best is always (l_lo, r_hi)
        
        heap = []
        
        def push(l_lo, l_hi, r_lo, r_hi):
            if l_lo > l_hi or r_lo > r_hi or l_lo > r_hi:
                return
            # best candidate in this region is always (l_lo, r_hi)
            # because extending l left or r right can only increase value
            actual_l = l_lo
            actual_r = r_hi
            if actual_l > actual_r:
                return
            val = st.query(actual_l, actual_r)
            heapq.heappush(heap, (-val, l_lo, l_hi, r_lo, r_hi))
        
        push(0, n - 1, 0, n - 1)
        
        ans = 0
        seen = set()
        
        for _ in range(k):
            while True:
                neg_val, l_lo, l_hi, r_lo, r_hi = heapq.heappop(heap)
                l, r = l_lo, r_hi  # actual subarray chosen
                if (l, r) not in seen:
                    break
            
            seen.add((l, r))
            ans += -neg_val
            
            # split into 4 quadrants, excluding current (l_lo, r_hi)
            # fix l=l_lo, shrink r: (l_lo, l_lo, r_lo, r_hi-1)
            push(l_lo, l_lo, r_lo, r_hi - 1)
            # fix r=r_hi, shrink l: (l_lo+1, l_hi, r_hi, r_hi)
            push(l_lo + 1, l_hi, r_hi, r_hi)
            # remaining quadrant: (l_lo+1, l_hi, r_lo, r_hi-1)
            push(l_lo + 1, l_hi, r_lo, r_hi - 1)
        
        return ans
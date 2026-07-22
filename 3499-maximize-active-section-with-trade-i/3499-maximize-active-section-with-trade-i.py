class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        active_count = 0
        max_inactive_pair_count = 0
        prev_inactive_block_count = float('-inf')

        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            block_len = j - i

            if s[i] == '1':
                active_count += block_len
            else:
                max_inactive_pair_count = max(max_inactive_pair_count, prev_inactive_block_count + block_len)
                prev_inactive_block_count = block_len

            i = j

        return active_count + max_inactive_pair_count
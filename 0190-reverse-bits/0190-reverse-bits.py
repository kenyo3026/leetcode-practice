class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0

        for _ in range(32):
            val = val << 1

            popped_bit = n & 1
            val = val | popped_bit

            n = n >> 1

        return val
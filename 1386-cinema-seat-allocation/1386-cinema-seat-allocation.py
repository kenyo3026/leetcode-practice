class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        blocks = [{2,3,4,5}, {4,5,6,7}, {6,7,8,9}]

        rows = defaultdict(set)
        for row, seat in reservedSeats:
            rows[row].add(seat)

        res = 2 * (n - len(rows))

        for row in rows:

            flags = [False, False, False]

            for seat in rows[row]:
                for i, block in enumerate(blocks):

                    if not flags[i] and seat in block:
                        flags[i] = True

            if not flags[0]:
                res += 1

            if not flags[2]:
                res += 1

            if flags[0] and flags[2] and not flags[1]:
                res += 1

        return res
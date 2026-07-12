class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_at, ranks = 1, {}

        for num in sorted(arr):
            if num in ranks:
                continue

            ranks[num] = rank_at
            rank_at += 1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr
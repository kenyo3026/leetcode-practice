class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        max_subset_len = 1

        for x in counts:

            if counts[x] < 2:
                continue

            if x == 1:
                subset_len = counts[x] - 1 if counts[x] % 2 == 0 else counts[x]

            else:
                subset_len = 0
                while x in counts:
                    if counts[x] >= 2:
                        subset_len += 2
                    elif counts[x] == 1:
                        subset_len += 1
                        break
                    else:
                        subset_len -= 1
                        break

                    x = x ** 2

                else:
                    subset_len -= 1

            max_subset_len = max(max_subset_len, subset_len)

        return max_subset_len
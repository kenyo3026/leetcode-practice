class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()

        for a, b, c in itertools.permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                nums.add(a * 100 + b * 10 + c)
        return len(nums)
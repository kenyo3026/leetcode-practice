class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        answer = []
        def separate(num) -> list:
            ans = []
            while num != 0:
                num, mod = num // 10, num % 10
                answer.append(mod)

        [separate(num) for num in nums[::-1]]
        return answer[::-1]
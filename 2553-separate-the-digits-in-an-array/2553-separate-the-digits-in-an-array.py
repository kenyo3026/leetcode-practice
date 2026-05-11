class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        def separate(num) -> list:
            ans = []
            while num != 0:
                num, mod = num // 10, num % 10
                ans.append(mod)
            return ans[::-1]

        answer = []
        for num in nums:
            ans = separate(num)
            answer.extend(ans)

        return answer
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {'1':set(), '>1':set()}

        for num in nums:
            if not num in num_count['1'] and not num in num_count['>1']:
                num_count['1'].add(num)
            elif not num in num_count['>1']:
                num_count['1'].remove(num)
                num_count['>1'].add(num)
            
        return next(iter(num_count['1']))
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # return [num for num in nums if num < pivot] + \
        #     [num for num in nums if num == pivot] + \
        #     [num for num in nums if num > pivot]
        left, middle, right = [], [], []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            elif num > pivot:
                right.append(num)

        return left + middle + right
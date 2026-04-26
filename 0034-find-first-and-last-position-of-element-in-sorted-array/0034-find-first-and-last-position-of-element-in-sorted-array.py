class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bs(nums, target, find:Literal['left', 'right']):
            left, right = 0, len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid

                    if find == 'left':
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return res
   
        return [bs(nums, target, 'left'), bs(nums, target, 'right')]
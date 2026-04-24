class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            w = right - left

            if height[left] > height[right]:
                h = height[right]
                right -= 1
            else:
                h = height[left]
                left += 1

            area = h * w
            if area > max_area:
                max_area = area

        return max_area
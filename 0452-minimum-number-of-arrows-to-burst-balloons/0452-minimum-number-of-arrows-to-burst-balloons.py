class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow_so_far = 1
        arrow_at = points[0][1]

        for xs, xe in points[1:]:
            if xs > arrow_at:
                arrow_so_far += 1
                arrow_at = xe

        return arrow_so_far

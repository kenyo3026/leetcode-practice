class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        overlapped = 0
        res = [intervals[0]]

        for interval in intervals[1:]:

            if res[-1][1] > interval[0]:
                overlapped += 1
                continue

            res.append(interval)

        return overlapped
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        overlapped = 0
        prev_interval = intervals[0]

        for interval in intervals[1:]:

            if prev_interval[1] > interval[0]:
                overlapped += 1
                continue

            prev_interval = interval

        return overlapped
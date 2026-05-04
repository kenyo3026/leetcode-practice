class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        inserted = []

        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            inserted.append(intervals[i])
            i += 1

        while i < n and not intervals[i][0] > newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i += 1
        inserted.append(newInterval)

        while i < n:
            inserted.append(intervals[i])
            i += 1

        return inserted
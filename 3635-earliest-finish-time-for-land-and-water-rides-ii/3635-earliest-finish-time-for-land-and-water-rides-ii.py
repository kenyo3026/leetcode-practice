class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n_land, n_water = len(landStartTime), len(waterStartTime)

        def f(start_time_1, duration_1, start_time_2, duration_2):
            finish_1 = min([start_1 + dur_1 for start_1, dur_1 in zip(start_time_1, duration_1)])
            return min(max(finish_1, start_2) + dur_2 for start_2, dur_2 in zip(start_time_2, duration_2))

        return min(
            f(landStartTime, landDuration, waterStartTime, waterDuration),
            f(waterStartTime, waterDuration, landStartTime, landDuration),
        )
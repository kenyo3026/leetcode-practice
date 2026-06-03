class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n_land, n_water = len(landStartTime), len(waterStartTime)
        min_both_finish = float('inf')

        def f(min_both_finish, start_time_1, duration_1, start_time_2, duration_2):
            finish_1 = min([start_1 + dur_1 for start_1, dur_1 in zip(start_time_1, duration_1)])
            for start_2, dur_2 in zip(start_time_2, duration_2):
                min_both_finish = min(min_both_finish, max(finish_1, start_2) + dur_2)

            return min_both_finish

        min_both_finish = f(min_both_finish, landStartTime, landDuration, waterStartTime, waterDuration)
        min_both_finish = f(min_both_finish, waterStartTime, waterDuration, landStartTime, landDuration)
        return min_both_finish
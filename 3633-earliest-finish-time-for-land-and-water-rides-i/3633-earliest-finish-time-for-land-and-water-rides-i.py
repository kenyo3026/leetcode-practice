class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n_land, n_water = len(landStartTime), len(waterStartTime)
        min_needed = float('inf')

        # Land -> Water
        land_finish = min(
            start + duration for start, duration in zip(landStartTime, landDuration)
        )
        for w in range(n_water):
            land_first_finish = max(land_finish, waterStartTime[w]) + waterDuration[w]
            min_needed = min(min_needed, land_first_finish)

        # Water -> Land
        water_finish = min(
            start + duration for start, duration in zip(waterStartTime, waterDuration)
        )
        for l in range(n_land):
            water_first_finish = max(water_finish, landStartTime[l]) + landDuration[l]
            min_needed = min(min_needed, water_first_finish)

        return min_needed
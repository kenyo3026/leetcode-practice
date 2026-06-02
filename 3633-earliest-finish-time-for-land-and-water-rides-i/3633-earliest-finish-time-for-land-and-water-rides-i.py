class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n_land, n_water = len(landStartTime), len(waterStartTime)
        min_needed = float('inf')

        for l in range(n_land):
            for w in range(n_water):

                # Land -> Water
                land_finish = landStartTime[l] + landDuration[l]
                land_first_finish = max(land_finish, waterStartTime[w]) + waterDuration[w]

                # Water -> Land
                water_finish = waterStartTime[w] + waterDuration[w]
                water_first_finish = max(water_finish, landStartTime[l]) + landDuration[l]

                min_needed = min(min_needed, land_first_finish, water_first_finish)

        return min_needed
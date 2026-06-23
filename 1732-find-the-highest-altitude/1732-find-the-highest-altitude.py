class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain_altitude = 0
        highest_altitude = gain_altitude

        for g in gain:
            gain_altitude += g
            highest_altitude = max(highest_altitude, gain_altitude)

        return highest_altitude
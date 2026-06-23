class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour_cursor = hour + hour_offset
        hour_cursor = (hour % 12) + (minutes / 60)
        hour_angle = (hour_cursor / 12) * 360

        # minutes_cursor = minutes
        minutes_cursor = minutes
        minutes_angle = (minutes_cursor / 60) * 360

        print(hour_angle, minutes_angle)

        # if hour_angle > minutes_angle:
        #     return hour_angle - minutes_angle
        # else:
        #     return minutes_angle - hour_angle
        angle = abs(hour_angle - minutes_angle)
        return min(angle, 360 - angle)
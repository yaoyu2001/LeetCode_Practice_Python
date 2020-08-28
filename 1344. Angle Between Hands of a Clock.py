class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        if hour == 12:
            hour_c = (minutes / 60) * 5
        else:
            hour_c = hour * 5 + (minutes / 60) * 5

        dif = abs(minutes - hour_c) / 60
        return min(360 * dif, 360 - 360 * dif)

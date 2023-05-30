class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour = float(hour)
        minutes =  float(minutes)
        hour_angle = float((hour + minutes/60.0) * 30.0)

        minutes_angle = minutes * 6

        angle = abs(hour_angle - minutes_angle)
        return angle if angle < 180 else 360 - angle
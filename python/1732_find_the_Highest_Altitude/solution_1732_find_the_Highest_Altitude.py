class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr = max_altitude = 0
        for i in range(len(gain)):
            curr += gain[i]
            max_altitude = max(max_altitude, curr)
        return max_altitude


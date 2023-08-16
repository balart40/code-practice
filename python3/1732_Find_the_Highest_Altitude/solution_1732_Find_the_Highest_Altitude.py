class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        max_altitude = curr_altitude = 0
        n = len(gain)
        for i in range(1, n):
            curr_altitude += gain[i]
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude
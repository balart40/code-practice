import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)

        def how_many_hours_eating(k: int) -> int:
            hours = 0
            for pile in piles:
                hours += int(math.ceil(pile/k))
            return hours

        low, high = 1, max(piles)
        result = high
        while low <= high:
            k = (low + high) // 2
            hours = how_many_hours_eating(k)
            if hours <= h:
                result = k
                high = k -1
            else:
                low = k + 1
        return result
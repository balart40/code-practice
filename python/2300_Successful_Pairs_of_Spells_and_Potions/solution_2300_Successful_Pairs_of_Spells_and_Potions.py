class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = []
        n = len(spells)
        m = len(potions)
        potions.sort()
        for spell in spells:
            success_counter = 0
            low = 0
            high = m - 1
            while low <= high:
                mid = (low + high) // 2
                product = potions[mid] * spell
                if product < success:
                    low = mid + 1
                else:
                    high = mid - 1
            pairs.append(m - low)
        return pairs
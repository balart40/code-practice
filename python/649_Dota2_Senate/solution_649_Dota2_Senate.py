class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # first pass
        r = []
        d = []
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        n = len(senate)
        while r and d:
            curr_r = r.pop(0)
            curr_d = d.pop(0)
            if curr_r < curr_d:
                r.append(n + curr_r)
            else:
                d.append(n + curr_d)
        return "Radiant" if r else "Dire"

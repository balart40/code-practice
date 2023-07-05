class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        d = dict()
        ans = 0
        # table of frequencies
        for task in tasks:
            d[task] = d.get(task, 0) + 1

        for val in d.values():
            if val == 1:
                return -1
            elif val % 3 == 0:
                ans += val // 3
            elif val % 3 == 1:
                ans += (val // 3) + 1
            elif val % 3 == 2:
                ans += (val // 3 )+ 1
        return ans
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        n = len(logs)
        user_times = dict()
        for i in range(n):
            if not user_times.get(logs[i][0], False):
                user_times[logs[i][0]] = set()
            user_times[logs[i][0]].add(logs[i][1])

        result = [0] * k
        for v in user_times.values():
            result[len(v)-1] += 1

        return result
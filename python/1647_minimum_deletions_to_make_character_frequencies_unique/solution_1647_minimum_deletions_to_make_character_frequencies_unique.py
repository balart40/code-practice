class Solution(object):

    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        n = len(s)
        f = dict()
        # capture frequencies
        for i in range(n):
            f[s[i]] = f.get(s[i], 0) + 1

        # get frequencies and negate them
        nums = [ -num for num in f.values()]
        # build heap with frequencies where
        # the most negative is smalles and therefore the most frequent
        heapq.heapify(nums)
        # store frequencies so they no repeat
        frequency_set = set()

        while nums:
            # get most frequent
            first = heapq.heappop(nums)
            # if frequency is not repeated add
            if first not in frequency_set:
                frequency_set.add(first)
                # no deletion continue
            else:
                deletions += 1
                # we need to delete so add to negative frequencies
                first += 1
                # if frequency is not zero re-enter in heap
                if first:
                    heapq.heappush(nums, first)
        return deletions

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        seen = []
        i = 1
        # counter of mod n % i where  == 0
        count = 0
        while i <= n:
            modul = n % i
            if modul == 0:
                seen.append(i)
                count += 1
                if count == k:
                    return i
            i += 1
        # if we reach here the list is smaller than k
        return -1
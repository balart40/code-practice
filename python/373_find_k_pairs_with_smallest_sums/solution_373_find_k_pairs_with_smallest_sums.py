import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        '''
        if k == 1:
            return [nums1[0], nums2[2]]
        result = []
        while nums1:
            current = nums1.pop(0)
            for i in range(len(nums2)):
                result.append([[current, nums2[i]], current+nums2[i]])
        result.sort(key=lambda x:x[1])
        for i in range(len(result)):
            result[i] = result[i][0]
        return result[0:k]

        if k == 1:
            return [nums1[0], nums2[2]]
        result = []
        i = 0
        j = 0
        while nums1:
            current = nums1.pop(0)
            for i in range(len(nums2)):
                heapq.heappush(result, [[current + nums2[i]],[current, nums2[i]]])
        result = heapq.nsmallest(k, result)
        for i in range(len(result)):
            result[i] = result[i][1]
        return result[0:k]
        '''
        h = []
        result = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            summ = nums1[i] + nums2[0]
            heapq.heappush(h, (summ, i, 0))
        while len(result) < k and h:
            _, u, v = heapq.heappop(h)
            result.append([nums1[u], nums2[v]])
            v_next = v + 1
            if v_next < m:
                summ = nums1[u] + nums2[v_next]
                heapq.heappush(h, (summ, u, v_next))
        return result


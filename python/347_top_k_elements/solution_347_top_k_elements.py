class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicto = dict()
        for i in range(len(nums)):
            if dicto.get(nums[i], None) == None:
                dicto[nums[i]] = [nums[i],1]
            else:
                dicto[nums[i]][1] += 1

        listOfTuples = dicto.values()
        heapq.heapify(listOfTuples)

        nlargest = heapq.nlargest(k,listOfTuples, key=lambda x : x[1])
        result = [ tupp[0] for tupp in nlargest]
        return result


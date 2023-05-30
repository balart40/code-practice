class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        if arr == []:
            return False
        n = len(arr)
        ocurrences = dict()
        for i in range(n):
            seen = ocurrences.get(arr[i], None)
            if seen:
                ocurrences[arr[i]]+=1
            else:
                ocurrences[arr[i]] = 1
        ocurrencesVals = ocurrences.values()
        numOcurrences = len(ocurrencesVals)
        numUniqueOcurrences = len(set(ocurrencesVals))
        if numUniqueOcurrences < numOcurrences:
            return False
        else:
            return True
        """
        if arr == []:
            return "false"

        ocurrences = dict()

        for i in range(len(arr)):
            ocurrences[arr[i]] = ocurrences.get(arr[i], 0) + 1

        return len(ocurrences.values()) == len(set(ocurrences.values()))
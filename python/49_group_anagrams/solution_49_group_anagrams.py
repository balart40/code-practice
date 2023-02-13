class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n == 1:
            return [strs]
        strs_two = []
        for i in range(n):
            strs_two.append([strs[i], ''.join(sorted(strs[i]))])
        strs_two = sorted(strs_two, key=lambda x: x[1])
        currLst = [strs_two[0][0]]
        result = []
        for i in range(1, len(strs_two)):
            if strs_two[i][1] != strs_two[i-1][1]:
                result.append(currLst)
                currLst = [strs_two[i][0]]
            else:
                currLst.append(strs_two[i][0])
        if currLst not in result:
            result.append(currLst)
        return result


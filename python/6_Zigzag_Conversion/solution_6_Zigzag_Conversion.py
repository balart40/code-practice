class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        result = ""
        grid = [''] * numRows
        index = 0
        step = 1 # start step down
        for char in  s:
            grid[index] += char
            if index == 0:
                # start goinf down
                step = 1
            # reach bottom go up
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(grid)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        n = len(height)
        result = [0]* n * n
        heightTuples =  []
        dimensions = []
        for i in range(n):
            heightTuples.append([height[i],i])
        heightTuplesCopy = list(heightTuples)

        for i in range(n):
            #rotate once
            temp = heightTuplesCopy.pop(0)
            heightTuplesCopy.append(temp)
            dimensions += zip(heightTuples, heightTuplesCopy)

        maxArea = 0
        for i in range(len(dimensions)):
            bar1, bar2 = dimensions[i]
            height1, idx1 = bar1
            height2, idx2 = bar2
            if height1 == 0 or height2 == 0 or (height1 == height2 and idx1 == idx2):
                continue
            else:
                base = abs(idx1-idx2)
                realHeight = min(height1, height2)
                area = base * realHeight
                if area >= maxArea:
                    maxArea = area
        return maxArea
        '''
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

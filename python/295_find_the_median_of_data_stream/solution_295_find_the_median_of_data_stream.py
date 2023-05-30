class MedianFinder(object):

    def __init__(self):
        self.small = [] # the smaller half of the list, max heap (invert min-heap)
        self.large = [] # the larger half of the list, min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        # even
        if len(self.large) ==  len(self.small):
            # negative since small has inverted nums
            return (self.large[0] -  self.small[0])/2.0
        else:
            return self.large[0]

#class MedianFinder(object):

    #def __init__(self):
        """
        self.nums = []
        self.median = None
        """
    #def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #self.nums.append(num)

    #def findMedian(self):
        """
        :rtype: float
        """
        """
        n = len(self.nums)
        half =  n //2
        self.nums.sort()
        self.median = self.nums[half] if n % 2 != 0 else (self.nums[half-1] + self.nums[half])/2.0
        return self.median
        """
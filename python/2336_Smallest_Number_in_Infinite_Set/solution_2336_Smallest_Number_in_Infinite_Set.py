class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        for i in range(1,1001):
            heapq.heappush(self.heap, i)


    def popSmallest(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.heap)


    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.heap:
            heapq.heappush(self.heap, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
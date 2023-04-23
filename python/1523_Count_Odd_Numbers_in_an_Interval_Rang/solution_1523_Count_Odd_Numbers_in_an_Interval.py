class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        #count = 0
        #arr = [number for number in range(low, high+1) if number % 2 != 0 ]
        #return len(arr)
        low += 1 if low % 2 == 0 else 0
        high -= 1 if high % 2 == 0 else 0
        return (high - low)//2+1
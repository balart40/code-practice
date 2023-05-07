class HitCounter(object):

    def __init__(self):
        self.timeStampList = [0] * 300
        self.countHits = [0] * 300

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        idx = timestamp % 300
        # we are no longer in the same 300 sec window
        if self.timeStampList[idx] != timestamp:
            # reset counter
            self.countHits[idx] = 1
            # store time in mod idx
            self.timeStampList[idx] = timestamp
        # if we get hit it same time again
        else:
            self.countHits[idx] += 1


    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        timeWindow = timestamp - 300
        hits = 0
        for i in range(300):
            # hit is in time window add the hits of such time
            if self.timeStampList[i] > timeWindow:
                hits += self.countHits[i]
        return hits
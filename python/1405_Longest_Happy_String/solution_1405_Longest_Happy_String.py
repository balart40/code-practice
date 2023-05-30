class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        result = ""
        maxRep = 3
        dicto = {"a" : a, "b": b, "c": c}

        while (sum(dicto.values()) != 0):
            min_key, mid_key, max_key = sorted(dicto, key=dicto.get)
            if dicto[mid_key] >= 1:
                if not result or result[-1] != max_key:
                    # we will add 2 max reps or less if we have less than 2
                    result += max_key * min(2, dicto[max_key])
                    # substract remaining
                    dicto[max_key] -= min(2, dicto[max_key])
                # add mid key which is at least 1
                result += mid_key
                dicto[mid_key] -= 1
            else:
                # without mid_key at least 1 we finish
                result += max_key * min(2, dicto[max_key])
                break
        return result
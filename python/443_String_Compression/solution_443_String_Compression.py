class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s =  ""
        prev = ""
        repeats = 0
        for i in range(len(chars)):
            if i == 0:
                prev = chars[i]
                repeats = 1
            else:
                if chars[i] == prev:
                    repeats += 1
                else:
                    s += prev
                    s += str(repeats) if repeats > 1 else ""
                    prev = chars[i]
                    repeats = 1
            if i == len(chars) - 1:
                s += chars[i]
                s += str(repeats) if repeats > 1 else ""
        s = list(s)
        n = len(s)
        chars[0:n] = s
        return n
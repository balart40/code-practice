class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(1, n):
            curr = s[0]
            temp = ""
            count = 0
            for char in s:
                if curr ==  char:
                    count += 1
                else:
                    temp += str(count) + curr
                    count = 1
                    curr = char
            temp += str(count) + curr
            s = temp
        return s

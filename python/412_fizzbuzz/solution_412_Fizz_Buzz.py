class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        three = "Fizz"
        five = "Buzz"
        result = list()
        num = 1
        while num <= n:
            curr = ""
            if num % 3 == 0 and num % 5 == 0:
                curr += three + five
            elif num % 3 == 0:
                curr += three
            elif num % 5 == 0:
                curr += five
            else:
                curr += str(num)
            result.append(curr)
            num += 1
        return result
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if(i % 3 == 0):
                if(i % 5 == 0 ):
                    result.append(str("FizzBuzz"))
                else:
                    result.append(str("Fizz"))
            elif (i % 5 == 0):
                result.append(str("Buzz"))
            else:
                result.append(str(i))
        return result

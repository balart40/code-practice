class Solution:
    def __init__(self) -> None:
        self.operator = {
            '+' : add,
            '-' : sub,
            '*' : mul
        }
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit(): return [int(expression)]
        result = []
        for i, char in enumerate(expression):
            if char in self.operator:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for num1 in left:
                    for num2 in right:
                        result.append(self.operator[char](num1, num2))

        return result
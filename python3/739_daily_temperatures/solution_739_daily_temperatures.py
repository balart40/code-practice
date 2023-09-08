class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # monotonic decreasing stack [temp, idx]
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                temp, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temperature, i))
        return result
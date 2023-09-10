class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, height in enumerate(heights):
            while stack and height >= stack[-1][1]:
                stack.pop()
            stack.append([idx, height])
        return [s[0] for s in stack]
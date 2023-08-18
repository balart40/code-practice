import numpy as np
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        while asteroids != []:
            curr = asteroids.pop(0)
            if not stack:
                stack.append(curr)
            else:
                while stack and stack[-1] > 0 and curr < 0:
                    if abs(stack[-1]) < abs(curr):
                        stack.pop()
                    elif abs(stack[-1]) == abs(curr):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(curr)
        return stack
from typing import List
from collections import deque


class Solution(object):

    def getMaximumEatenDishCount(self, N: int, D: List[int], K: int) -> int:
        counter = 0
        queue = deque()
        eaten = dict()

        for sushi in D:
            if sushi in eaten:
                continue
            else:
                counter += 1
                queue.append(sushi)
                if len(queue) > K:
                    to_remove = queue.popleft()
                    del eaten[to_remove]
                eaten[sushi] = True
        return counter
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                # first
                if i == 0:
                    if len(flowerbed) ==  1 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                    elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                # 1 onwards
                else:
                    # last one
                    if i == len(flowerbed) - 1:
                        if flowerbed[i - 1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                    # non last one
                    elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            i += 1
        return True if n == 0 else False
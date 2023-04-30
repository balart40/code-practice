class Solution(object):

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        def sign(num):
            if num < 0:
                return -1
            if num > 0:
                return 1
            return 0

        global_visited = set()

        for i in range(n):
            if i in global_visited:
                continue
            curr_visited = set()
            j =  i
            while True:
                if not j in curr_visited:
                    curr_visited.add(j)
                    nextJump = (j + nums[j]) % n
                    if j == nextJump or sign(nums[i]) != sign(nums[nextJump]) or nextJump in global_visited:
                        global_visited = global_visited.union(curr_visited)
                        break
                    j = nextJump
                else:
                    return True
        return False

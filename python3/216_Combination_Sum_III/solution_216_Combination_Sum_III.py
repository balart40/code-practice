class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def dfs_backtracking(k: int, n: int, nums: List[int], path: List[int]) -> List[List[int]]:
            nonlocal result
            if k < 0 or n < 0:
                return
            if k == 0 and n == 0:
                result.append(path)
            for i in range(len(nums)):
                dfs_backtracking(k-1, n-nums[i], nums[i + 1:], path + [nums[i]])

        dfs_backtracking(k, n, list(range(1,10)), [])
        return result
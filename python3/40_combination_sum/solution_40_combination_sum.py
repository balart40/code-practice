class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs_backtracking(n: int, nums: List[int], path: List[int]):
            nonlocal result
            if n < 0:
                return
            if n == 0:
                result.add(tuple(path))
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] > n:
                    break
                dfs_backtracking(n-nums[i], nums[i + 1:], path + [nums[i]])
            return

        dfs_backtracking(target, sorted(candidates), [])
        return list(result)
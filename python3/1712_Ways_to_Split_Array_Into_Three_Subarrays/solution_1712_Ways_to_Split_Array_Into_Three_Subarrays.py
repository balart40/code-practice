class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        n = len(nums)
        result = j = k = 0
        for i in range(1, n):
            j = max(j, i + 1)
            while j < n and 2*prefix_sum[i] > prefix_sum[j]:
                j += 1
            k = max(k, j)
            while k < n and 2*prefix_sum[k] <= prefix_sum[i] + prefix_sum[-1]:
                k += 1
            result += k - j
        return result  % 1_000_000_007
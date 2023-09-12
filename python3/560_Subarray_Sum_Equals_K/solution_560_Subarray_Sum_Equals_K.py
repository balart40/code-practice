class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        curr_prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            curr_prefix_sum += nums[i]
            remainder_to_search = curr_prefix_sum - k

            if remainder_to_search in prefix_sum:
                result += prefix_sum[remainder_to_search]
            prefix_sum[curr_prefix_sum] += 1
        return result
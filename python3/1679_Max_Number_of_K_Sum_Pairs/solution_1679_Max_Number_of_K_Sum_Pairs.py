class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(lambda: 0)
        counter = 0
        for i in range(len(nums)):
            num_to_search = k - nums[i]
            if num_to_search in d and d[num_to_search] > 0:
                counter += 1
                d[num_to_search] -= 1
            elif nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return counter
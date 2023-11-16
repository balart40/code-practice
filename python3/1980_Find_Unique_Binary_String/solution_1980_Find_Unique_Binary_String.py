class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        max_num = 2**(n) - 1
        d = collections.defaultdict(str)
        result = ""
        for num in nums:
            d[num] = num
        for i in range(max_num + 1):
            bin_num = bin(i)[2:].zfill(n)
            if bin_num not in d:
                return bin_num
        return result
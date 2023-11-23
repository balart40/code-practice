class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [True] * len(l)
        for i in range(len(r)):
            curr_len = r[i] - l[i] + 1
            if curr_len < 2:
                result[i] = True
            else:
                sub_array = sorted(nums[l[i] : r[i] + 1])
                diff = sub_array[1] - sub_array[0]
                for j in range(2, len(sub_array)):
                    if (sub_array[j] - sub_array[j -1]) != diff:
                        result[i] = False
                        break
        return result
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        list1 = list(nums1 - nums2)
        list2 = list(nums2 - nums1)
        return [list1, list2]



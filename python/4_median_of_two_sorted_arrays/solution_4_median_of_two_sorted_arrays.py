class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def mergeSortedList(nums1, nums2):
            result = []
            while nums1 != [] or nums2 != []:
                if nums1 != [] and nums2 !=[]:
                    if nums1[0] < nums2[0]:
                        result.append(nums1.pop(0))
                    else:
                        result.append(nums2.pop(0))
                elif nums2 == []:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            return result

        merged_list = mergeSortedList(nums1, nums2)
        n = len(merged_list)
        if n % 2 == 0:
            return float((merged_list[n//2-1] + merged_list[n//2]) / 2.0)
        else:
            return float(merged_list[n // 2])
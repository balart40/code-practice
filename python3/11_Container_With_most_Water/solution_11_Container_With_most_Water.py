class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = curr_area = 0
        left = 0
        right = n - 1
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            if height[right] <= height[left]:
                right -= 1
            else:
                left +=1
        return max_area
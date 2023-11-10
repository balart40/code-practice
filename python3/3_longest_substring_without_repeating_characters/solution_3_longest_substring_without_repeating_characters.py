class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = collections.defaultdict(int)
        left = right = max_len = 0
        while right < len(s):
            if s[right] not in seen:
                max_len = max(max_len, right - left + 1)
            else:
                if seen[s[right]] < left:
                    max_len = max(max_len, right - left + 1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
            right += 1
        return max_len
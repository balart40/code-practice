class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        queue = collections.deque([i for i in range(haystack_len) if haystack[i] == needle[0]])

        while queue:
            i = queue.popleft()
            result = i if haystack[i:i+needle_len] == needle else -1
            if result != -1:
                return result
        return -1
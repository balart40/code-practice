class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        queue = collections.deque()

        for i in range(haystack_len):
            if haystack[i] == needle[0]:
                queue.append(i)

        if not queue:
            return -1

        while queue:
            i = queue.popleft()
            result = i if haystack[i:i+needle_len] == needle else -1
            if result != -1:
                return result
        return -1
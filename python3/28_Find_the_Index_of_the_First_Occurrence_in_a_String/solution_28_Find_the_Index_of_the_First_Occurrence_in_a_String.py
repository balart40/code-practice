class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        stack =  [i for i in range(haystack_len) if haystack[i] == needle[0]]

        if not stack:
            return -1

        def search_ocurrence(j: int) -> int:
            curr_idx = 0
            idx = -1
            for i in range(j, haystack_len):
                if haystack[i] == needle[curr_idx]:
                    if curr_idx == 0:
                        idx = i
                    curr_idx += 1
                    if curr_idx == needle_len:
                        return idx
                else:
                    return -1
            return -1

        while stack:
            i = stack.pop(0)
            result = search_ocurrence(i)
            if result != -1:
                return result
        return -1
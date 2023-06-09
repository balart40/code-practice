class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_str = ""
        curr_num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            if s[i] == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif s[i] == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str +  curr_str * prev_num
            elif s[i] in string.ascii_letters:
                curr_str += s[i]
        while stack:
            curr_str = stack.pop() + curr_str
        return curr_str
class Solution:
    def decodeString(self, s: str) -> str:
        nums_stack = []
        string_stack = []
        num_str = ""
        result = ""
        for char in s:
            if char.isdigit():
                num_str += char
            elif char.isalpha():
                result += char
            elif char == "[":
                nums_stack.append(int(num_str))
                string_stack.append(result)
                num_str = ""
                result = ""
            elif char == "]":
                result = string_stack.pop() + nums_stack.pop()*result
        return result
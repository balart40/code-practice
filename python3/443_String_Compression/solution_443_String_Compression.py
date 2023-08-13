class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) ==  1:
            return 1
        i = len(chars) - 2
        count = 1
        while i >= 0:
            if chars[i] == chars[i + 1]:
                count += 1
                chars.pop(i + 1)
                if i == 0:
                    for num in reversed(str(count)):
                        chars.insert(i+1, str(num))
            else:
                if count != 1:
                    char = chars.pop(i +1)
                    for num in reversed(str(count)):
                        chars.insert(i+1, str(num))
                    chars.insert(i+1, char)
                    count = 1
            i -= 1
        return len(chars)

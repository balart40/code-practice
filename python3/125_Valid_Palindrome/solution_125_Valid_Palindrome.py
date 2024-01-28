class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s =  s.replace(" ", "")
        for punc in string.punctuation:
            s = s.replace(punc, "")
        return s == s[::-1]

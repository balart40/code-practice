import math


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        '''
         n = len(palindrome)
        if n == 1:
            return ""
        if n % 2 == 0:
            idx = n/2
        else:
            idx = int(math.floor(n/2))
        idx -= 1
        alphabet_dict = {}
        for i in range(26):
            letter = chr(ord('a') + i)
            alphabet_dict[letter] = i
        alphabet_list = [chr(ord('a') + i) for i in range(26)]
        currChar = ""
        i = 0
        while i <= idx:
            currChar = palindrome[i]
            currCharVal = alphabet_dict.get(currChar, 25)
            for j in range(26):
                if j < currCharVal and j != currCharVal:
                    palindrome = palindrome.replace(currChar,alphabet_list[j], 1)
                    return palindrome
            i += 1
        return palindrome[:-1]+"b"
        '''
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"

class Solution:
    ### solution without list
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        result = curr = ""
        n = len(s)
        for i in range(n):
            if i == n - 1:
                if result == "":
                    result = curr + s[i]
                else:
                    result = curr + s[i]  + " " + result
            elif s[i] != " ":
                curr += s[i]
            else:
                if result == "":
                    result = curr
                else:
                    result = curr + " " + result if curr else result
                curr = ""
        return result
        ##solution with list
        #s = s.strip()
        #s = s.split()
        #s = s[::-1]
        #return ' '.join(s)
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # str1 is the largest string always
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str1 == str2:
            return str1
        # if str1 does not start with str2
        if str1[:len(str2)] != str2:
            return ""
        # recursive with str1 without the str2 seen at then of str1
        return self.gcdOfStrings(str1[:len(str2)],str2)


        ############## EXPLAINED ##################
        #           Str1        str2
        # 1 rec    ABCABC       ABC  ->first if compare ABC vs ABC equal so continue
        # 2 rec    ABC___       ABC   -> they are equal so return ABC

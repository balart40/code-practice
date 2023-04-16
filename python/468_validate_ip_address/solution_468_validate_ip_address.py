import string

class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        NEITHER = "Neither"
        isIpv4 = len(queryIP.split('.')) == 4
        isIpv6 = len(queryIP.split(':')) == 8
        if((not isIpv4) and (not isIpv6)):
            return NEITHER
        if isIpv4:
            isIpv4Split = queryIP.split('.')
            for i in range(4):
                iPStr = isIpv4Split[i]
                if not iPStr.isdigit() or len(iPStr) > 3 or (iPStr[0] == '0' and len(iPStr) > 1) or int(iPStr) < 0 or int(iPStr) > 255:
                    return NEITHER
            return "IPv4"
        elif isIpv6:
            isIpv6Split = queryIP.split(':')
            for i in range(8):
                iPStr = isIpv6Split[i]
                if len(iPStr) > 4 or len(iPStr) == 0:
                    return NEITHER
                for c in iPStr:
                    if c not in string.hexdigits:
                        return NEITHER
            return "IPv6"
        return NEITHER
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Make a the shorter string
        if len(a) > len(b):
            tmp = a
            a = b
            b = tmp
        # Make a as long as b
        a = ''.join(["0" for x in range(len(b)-len(a))]) + a
        res = ""
        carry = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == "0" and b[i] == "0":
                if carry == 1:
                    res += "1"
                    carry = 0
                else:
                    res += "0"
            elif a[i] == "1" and b[i] == "0" or a[i] == "0" and b[i] == "1":
                if carry == 1:
                    res += "0"
                else:
                    res += "1"
            else:
                if carry == 1:
                    res += "1"
                else:
                    res += "0"
                carry = 1
        if carry == 1:
                res += "1"
        return res[::-1]
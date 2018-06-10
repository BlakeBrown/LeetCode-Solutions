class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Make num1 shorter
        if len(num1) > len(num2):
           tmp = num1
           num1 = num2
           num2 = tmp
        # Make num1 as long as num2
        carry = 0
        total = 0
        for i in range(len(num1)):
            a = ord(num1[-i-1])-48
            res = ''.join(["0" for x in range(i)])
            carry = 0
            for j in range(len(num2)):
                b = ord(num2[-j-1])-48
                m = a*b + carry
                if m > 9:
                    carry = int(m/10)
                else:
                    carry = 0
                m %= 10
                res += str(m)
            res += str(carry)
            total += int(res[::-1])
        return str(total)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "10"
        s = "1"
        n -= 1
        while n != 0:
            count = 1
            c = s[0]
            s2 = ""
            for i in range(1,len(s)):
                if s[i] != s[i-1]:
                    s2 += (str(count)+s[i-1])
                    count = 1
                    c = s[i]
                else:
                    count += 1
            s2 += (str(count)+c)
            s = s2
            n -= 1
        return s
class Solution(object):
    def convertToTitle(self,n):
        """
        :type n: int
        :rtype: str
        """
        ret = ""
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        while True:
            if n <= 26:
                ret += letters[n-1]
                break
            else:
                nDiv = int((n-1)/26)
                power = 1
                while nDiv > 26:
                    nDiv = int(nDiv/26)
                    power += 1
                ret += letters[nDiv-1]
                n -= int(nDiv)*(26**power)
        return ret

                
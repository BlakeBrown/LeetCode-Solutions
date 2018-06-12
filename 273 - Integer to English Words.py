class Solution(object):
    def recursivelyPrint(self, num):
        if num == 0:
            return ""
        if num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        elif num == 9:
            return "Nine"
        elif num == 10:
            return "Ten"
        elif num == 11:
            return "Eleven"
        elif num == 12:
            return "Twelve"
        elif num == 13:
            return "Thirteen"
        elif num == 14:
            return "Fourteen"
        elif num == 15:
            return "Fifteen"
        elif num == 16:
            return "Sixteen"
        elif num == 17:
            return "Seventeen"
        elif num == 18:
            return "Eighteen"
        elif num == 19:
            return "Nineteen"
        elif num >= 20 and num < 30:
            return "Twenty " + self.recursivelyPrint(num-20)
        elif num >= 30 and num < 40:
            return "Thirty " + self.recursivelyPrint(num-30)
        elif num >= 40 and num < 50:
            return "Forty " + self.recursivelyPrint(num-40)
        elif num >= 50 and num < 60:
            return "Fifty " + self.recursivelyPrint(num-50)
        elif num >= 60 and num < 70:
            return "Sixty " + self.recursivelyPrint(num-60)
        elif num >= 70 and num < 80:
            return "Seventy " + self.recursivelyPrint(num-70)
        elif num >= 80 and num < 90:
            return "Eighty " + self.recursivelyPrint(num-80)
        elif num >= 90 and num < 100:
            return "Ninety " + self.recursivelyPrint(num-90)
        elif num >= 100 and num < 1000:
            return self.recursivelyPrint(int(num/100)) + " Hundred " + self.recursivelyPrint(num%100)
        elif num >= 1000 and num < 1000000:
            return self.recursivelyPrint(int(num/1000)) + " Thousand " + self.recursivelyPrint(num%1000)
        elif num >= 1000000 and num < 1000000000:
            return self.recursivelyPrint(int(num/1000000)) + " Million " + self.recursivelyPrint(num%1000000)
        elif num >= 1000000000 and num < 10000000000:
            return self.recursivelyPrint(int(num/1000000000)) + " Billion " + self.recursivelyPrint(num%1000000000)
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        else:
            return ' '.join(self.recursivelyPrint(num).split())

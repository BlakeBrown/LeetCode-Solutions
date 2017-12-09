class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        if(len(strs) == 0):
            return answer
        for i, c in enumerate(strs[0]):
            common = True
            for string in strs:
                if(len(string) == i or string[i] != c):
                    common = False
                    break
            if common == False:
                break
            else:
                answer += c
            
        return answer
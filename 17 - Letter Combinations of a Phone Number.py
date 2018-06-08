class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def recursiveCombine(s, letters, res):
            if len(s) == 0:
                return res.append(letters)
            mapping = mappings[s[0]]
            for c in mapping:
                recursiveCombine(s[1:],letters+c,res)
        res = []
        recursiveCombine(digits,"",res)
        return res
        
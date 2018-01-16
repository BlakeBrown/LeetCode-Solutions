class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedWordToIndexList = {}
        for i, str in enumerate(strs):
            sortedStr = ''.join(sorted(str))
            if sortedStr in sortedWordToIndexList:
                sortedWordToIndexList[sortedStr].append(str)
            else:
                sortedWordToIndexList[sortedStr] = [str]
        answer = []
        for key in sortedWordToIndexList:
            answer.append(sortedWordToIndexList[key])
        return answer
from collections import deque
class Solution(object):
    def isValidWindow(self,sCount,tCount):
        for key in tCount:
            if key not in sCount:
                return False
            if sCount[key] < tCount[key]:
                return False
        return True
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        # Count all the letters in t
        tCount = {}
        for c in t:
            if c in tCount:
                tCount[c] += 1
            else:
                tCount[c] = 1
        # We'll also count the letters in s as we go through the array
        sCount = {}
        queue = deque([])
        minWindow = ""
        for i,c in enumerate(s):
            if c not in tCount:
                continue
            if c in sCount:
                sCount[c] += 1
            else:
                sCount[c] = 1
            queue.append((c,i))
            if self.isValidWindow(sCount,tCount):
                # Minimize the window (slide to the right if possible)
                pair = None
                while len(queue) > 0 and self.isValidWindow(sCount,tCount):
                    pair = queue.popleft()
                    sCount[pair[0]] -= 1
                # Check if it's the minimum
                if minWindow == "" or i-pair[1]+1 < len(minWindow):
                    minWindow = s[pair[1]:i+1]
        return minWindow


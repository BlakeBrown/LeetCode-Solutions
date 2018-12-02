# Solution 1: Recursively calculate solution, hash to avoid duplicate solutions
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.solutions = set()
        self.candidates = candidates
        self.checkSolution(target, [])
        ans = []
        for solution in self.solutions:
            ans.append(list(solution))
        return ans

    def checkSolution(self, target, solution):
        if target <= 0:
            if target == 0:
                solution.sort()
                self.solutions.add(tuple(solution))
            return
        for candidate in self.candidates:
            newSolution = solution[:]
            newSolution.append(candidate)
            self.checkSolution(target - candidate, newSolution)

# Solution 2: Avoid generating duplicate solutions at all by keeping track of index
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.checked = set()
        self.solutions = []
        self.candidates = candidates
        self.checkSolution(target, [], 0)
        return self.solutions

    def checkSolution(self, target, solution, i):
        if target <= 0:
            if target == 0:
                self.solutions.append(solution)
            return
        while i < len(self.candidates):
            newSolution = solution[:]
            newSolution.append(self.candidates[i])
            self.checkSolution(target - self.candidates[i], newSolution, i)
            i += 1


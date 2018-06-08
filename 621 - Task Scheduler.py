# Solution 1: Count the number of each task. Observe that we should always do the largest task
# first, then the second largest, then the 3rd largest, ... until we no longer need to be idle
# and can repeat the largest task again. However, the largest task might change after
# a few iterations. So every time we go back to redo the largest task, we should resort the tasks
# in decreasing order.

# Runtime: O(sum of tasks). There are a maximum of 26 tasks, so sorting the tasks takes
# "constant" time. Furthermore we don't care what n is, since if we hit the end of our task
# array we just add the remaining n to our total.
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0 for x in range(26)]
        for task in tasks:
            count[ord(task)-65] += 1 # ord(task) = ascii value of task
        count = sorted(count,reverse=True)
        total = 0
        while count[0] != 0:
            remainingCycles = n+1
            for i in range(len(count)):
                if remainingCycles == 0:
                    break # we can go back and do the largest task
                if count[i] == 0:
                    # we completed every task we could do
                    if count[0] != 0:
                        total += remainingCycles
                    break
                # complete a task
                total += 1
                count[i] -= 1
                remainingCycles -= 1
            count = sorted(count,reverse=True)
        return total

# Solution 2: Note that we immediately know how to arrange the largest task. We perform it
# everytime we no longer need to idle.
# ex. Given 3 A, 2 B, 1 C, n = 2
# A ? ? A ? ? A
# We can just fill the ?'s with all other tasks
# A B C A B - A, - is idle
# So our answer is len(tasks) + # of idle cycles

# Let's try another example: A A A B B B, n = 2
# A ? ? A ? ? A ? ?
# A B - A B - A B, - is idle
# Again our answer is len(tasks) + # of idle cycles

# So how do we calculate the answer?
# wait time = n + 1 - number of max tasks
# cycles = (number of max tasks + wait time)*size of max task - wait time

# ex1. wait time = 2
# cycles = (1+2)*3-2 = 7

# ex2. wait time = 1
# cycles = (2+1)*3 - 1

# Note: We might have a negative wait time, in which case we don't need to 
# wait at all to complete a task. To fix this return max(len(tasks),cycles).

# O(n) runtime and O(1) space
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0 for x in range(26)]
        for task in tasks:
            count[ord(task)-65] += 1 # ord(task) = ascii value of task
        count = sorted(count,reverse=True)
        maxTasks = 1
        for i in range(1,26):
            if count[i] == count[i-1]:
                maxTasks += 1
            else:
                break
        waitTime = n+1-maxTasks
        cycles = (maxTasks+waitTime)*count[0] - waitTime
        return max(len(tasks),cycles)
                


# Solution: Use a stack to keep track of where we are in the NestedList. next() should just return
# the top of the stack. hasNext() should recursively pop from the stack and append items until
# the top of the stack is an integer or is empty.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[i])
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False
        if self.stack[-1].isInteger():
            return True
        obj = self.stack.pop()
        nestedList = obj.getList()
        for i in range(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[i])
        return self.hasNext()
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
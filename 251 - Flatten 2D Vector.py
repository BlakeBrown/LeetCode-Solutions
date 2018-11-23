class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d;
        self.rowIndex = 0;
        self.columnIndex = 0;

    def next(self):
        """
        :rtype: int
        """
        self.columnIndex += 1
        return self.vec2d[self.rowIndex][self.columnIndex-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.rowIndex >= len(self.vec2d):
            return False
        if self.columnIndex >= len(self.vec2d[self.rowIndex]):
            self.columnIndex = 0
            self.rowIndex += 1
            return self.hasNext()
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
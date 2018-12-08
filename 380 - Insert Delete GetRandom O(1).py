import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.nums = {}
        random.seed()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            return False
        self.nums[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.nums:
            return False
        i = self.nums[val]
        self.arr[i] = self.arr[-1]
        self.nums[self.arr[-1]] = i
        self.arr.pop()
        del self.nums[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.arr) == 0:
            return False
        return self.arr[random.randint(0,len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
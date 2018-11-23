# Solution 1: Relatively straight forward, just make sure to handle all the edges cases
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        fruit_one = 0
        fruit_one_type = None
        fruit_two = 0
        fruit_two_type = None
        max_fruit = 0
        for i in range(len(tree)):
            if fruit_one_type is None:
                fruit_one += 1
                fruit_one_type = tree[i]
                continue
            if tree[i] == fruit_one_type:
                fruit_one += 1
                continue
            if fruit_two_type is None:
                fruit_two += 1
                fruit_two_type = tree[i]
                continue
            if tree[i] == fruit_two_type:
                fruit_two += 1
                continue
            # If we get to this point, we've hit a new fruit type
            # Check if we have a bigger max and reset
            max_fruit = max(fruit_one + fruit_two, max_fruit)
            new_fruit_one = 1
            new_fruit_one_type = tree[i-1]
            for j in range(i-2,-1,-1):
                if tree[j] != new_fruit_one_type:
                    break
                new_fruit_one += 1
            fruit_one = new_fruit_one
            fruit_one_type = new_fruit_one_type
            fruit_two = 1
            fruit_two_type = tree[i]
        max_fruit = max(fruit_one + fruit_two, max_fruit)
        return max_fruit


# Solution 2: Avoid backtracking to guarantee O(n) solution
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) < 2:
            return len(tree)
        fruit_one = 0
        fruit_one_type = None
        fruit_two = 0
        fruit_two_type = None
        max_fruit = 0
        new_fruit_one = 1
        new_fruit_one_type = tree[0]
        for i in range(len(tree)):
            if i > 1 and tree[i-1] == new_fruit_one_type:
                new_fruit_one += 1
            else:
                new_fruit_one_type = tree[i-1]
                new_fruit_one = 1
            if fruit_one_type is None:
                fruit_one += 1
                fruit_one_type = tree[i]
                continue
            if tree[i] == fruit_one_type:
                fruit_one += 1
                continue
            if fruit_two_type is None:
                fruit_two += 1
                fruit_two_type = tree[i]
                continue
            if tree[i] == fruit_two_type:
                fruit_two += 1
                continue
            # If we get to this point, we've hit a new fruit type
            # Check if we have a bigger max and reset
            max_fruit = max(fruit_one + fruit_two, max_fruit)
            fruit_one = new_fruit_one
            fruit_one_type = new_fruit_one_type
            fruit_two = 1
            fruit_two_type = tree[i]
        max_fruit = max(fruit_one + fruit_two, max_fruit)
        return max_fruit
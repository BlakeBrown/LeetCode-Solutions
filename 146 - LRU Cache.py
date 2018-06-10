# Solution: Implement a doubly linked list and a hashtable to get both operations in O(1).

# Note: In Python we could use an OrderedDict to solve the question, but
# this defeats the purpose of the question since an OrderedDict is basically an LRU cache
# under the hood. We should implement our own solution instead.

# Tip #1: Use a tail pointer instead of creating cycles in the DLL
# (i.e don't use head.prev to get tail)

# Tip #2: Remember to remove ALL pointers (including those on the node itself) when you
# remove a node

# Node is an object in a DLL
class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
    
    # Adds a node to the front of the DLL
    def addNode(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node       
        if self.tail is None:
            self.tail = node

    # Removes a node from the DLL
    def removeNode(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        # Gotcha: Need to remove the pointers on the node itself in case you add it back in
        node.next = None
        node.prev = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            # Move node to front of DLL
            self.removeNode(node)
            self.addNode(node)
            return node.value
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            # Key is already in cache, just need to update it's value and it to the front
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)

        else:
            # We're adding a new key to the cache
            if self.capacity > 0:
                self.capacity -=1
            else:
                # Delete tail of DLL
                del self.cache[self.tail.key]
                self.removeNode(self.tail)
            node = Node(key,value)
            self.cache[key] = node
            self.addNode(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
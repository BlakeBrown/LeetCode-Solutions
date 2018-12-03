# Solution 1: Use sets to continuously merge routes until we can reach the destination
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        # Convert every route to a set
        busRoutes = []
        for route in routes:
            busRoutes.append(set(route))
        # Find a starting bus
        i = 0
        while i < len(busRoutes):
            if busRoutes[i] & set([S]):
                break
            i += 1
        if i == len(routes):
            return -1 # no starting bus
        # Merge all other possible starting bus routes together
        j = i+1
        while j < len(busRoutes):
            if busRoutes[j] & set([S]):
                busRoutes[i] |= busRoutes[j]
                busRoutes.pop(j)
            else:
                j += 1
        reachableStops = busRoutes[i]
        busRoutes.pop(i)
        # Keep merging bus routes together till we can reach the destination 
        ans = 1
        while len(busRoutes) > 0:
            if reachableStops & set([T]):
                return ans
            deepCopy = set(list(reachableStops))
            j = 0
            merged = False
            while j < len(busRoutes):
                if deepCopy & busRoutes[j]:
                    reachableStops |= busRoutes[j]
                    busRoutes.pop(j)
                    merged = True
                else:
                    j += 1
            if not merged:
                break
            ans += 1
        if reachableStops & set([T]):
            return ans
        return -1

# Solution 2: list.pop() takes O(n) time in the worst case,
# we can cleverly avoid this by just emptying the set at the given index

# Also we don't need to use intersection for a single element, we can just check
# if the element exists in the set *whoops* 😅
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        # Convert every route to a set
        busRoutes = []
        for route in routes:
            busRoutes.append(set(route))
        # Find a starting bus
        i = 0
        while i < len(busRoutes):
            if S in busRoutes[i]:
                break
            i += 1
        if i == len(routes):
            return -1 # no starting bus
        # Merge all other possible starting bus routes together
        j = i+1
        while j < len(busRoutes):
            if S in busRoutes[j]:
                busRoutes[i] |= busRoutes[j]
                busRoutes[j] = set()
            j += 1
        reachableStops = busRoutes[i]
        busRoutes[i] = set()
        # Keep merging bus routes together till we can reach the destination 
        ans = 1
        while len(busRoutes) > 0:
            if T in reachableStops:
                return ans
            deepCopy = set(list(reachableStops))
            j = 0
            merged = False
            while j < len(busRoutes):
                if deepCopy & busRoutes[j]:
                    reachableStops |= busRoutes[j]
                    busRoutes[j] = set()
                    merged = True
                else:
                    j += 1
            if not merged:
                break
            ans += 1
        if T in reachableStops:
            return ans
        return -1
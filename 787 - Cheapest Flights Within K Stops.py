# Solution 1: Do a BFS starting from source.
import math
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flightLookup = {}
        for f in flights:
            if f[0] in flightLookup:
                flightLookup[f[0]].append(f)
            else:
                flightLookup[f[0]] = [f]
        # Handle edge cases
        if src == dst:
            return 0
        if src not in flightLookup:
            return -1
        # BFS
        cost_to_city = [math.inf] * n
        cost_to_city[src] = 0
        cities = set([src])
        for i in range(K+1):
            new_cities = set()
            new_cost_to_city = cost_to_city[:]
            while len(cities) > 0:
                city = cities.pop()
                if city not in flightLookup:
                    continue
                for flight in flightLookup[city]:
                    s = flight[0]
                    d = flight[1]
                    c = flight[2]
                    new_cost_to_city[d] = min(new_cost_to_city[d], cost_to_city[s] + c)
                    new_cities.add(d)
            cities = new_cities
            cost_to_city = new_cost_to_city
        if cost_to_city[dst] is math.inf:
            return -1
        return cost_to_city[dst]

from collections import defaultdict


# from queue import PriorityQueue as PQ

class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        # First build graph
        self.flights = defaultdict(list)

        for f, d in tickets:
            self.flights[f].append(d)

        self.visited = {}

        # sort the itinerary based on the lexical order
        # Use a map to indicate visit condition of every des from a origin
        for origin, itinerary in self.flights.items():
            itinerary.sort()
            self.visited[origin] = [False] * len(itinerary)

        self.flights_num = len(tickets)  # Total num of flights
        self.res = []
        route = ['JFK']
        self.backtrack('JFK', route)

        return self.res

    def backtrack(self, origin, route):
        # In this case we have traversal all nodes
        if len(route) == self.flights_num + 1:
            self.res = route
            return True

        # Traversal all nodes of origin node,
        for idx, nextDes in enumerate(self.flights[origin]):
            if not self.visited[origin][idx]:  # judge if a node is visited
                self.visited[origin][idx] = True
                ret = self.backtrack(nextDes, route + [nextDes])
                # That means we got a block and cant get the full map, so we backtrack
                self.visited[origin][idx] = False

                if ret: # current route if finished
                    return True

        return False


so = Solution()
print(so.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
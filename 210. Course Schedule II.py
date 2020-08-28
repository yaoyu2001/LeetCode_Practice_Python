from collections import defaultdict
class Solution:
    WHITE = 1 # Node not visited
    GRAY = 2 # Node in traversal
    BLACK = 3 # Node finish
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:

        # Create a adjacency list to store nodes and represent graph
        adj_list = defaultdict(list)

        # [a, b] -> a edge from node b to node a
        for destination, origin in prerequisites:
            adj_list[origin].append(destination)

        # TP sort as a stack, from bot to top will be the final order
        topological_sorted = []
        # If has circle, return an empty list
        no_circle = True

        # Use color to indicate condition, default condition is WHITE

        color = {k : Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal no_circle

            # If find a circle, we need't to go on
            if not no_circle:
                return

            # Start recursion
            color[node] = Solution.GRAY

            for neighbor in adj_list[node]:
                if color[neighbor] == Solution.WHITE:
                    dfs(neighbor)
                elif color[neighbor] == Solution.GRAY: # Find circle !
                    no_circle = False

            # Finish recursion
            color[node] = Solution.BLACK
            topological_sorted.append(node)

        for v in range(numCourses):
            if color[v] == Solution.WHITE:
                dfs(v)

        return topological_sorted[::-1] if no_circle else []


num = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

so = Solution()
print(so.findOrder(num, prerequisites))




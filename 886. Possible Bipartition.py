import collections

class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, 1-c) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)

    def if_not_circle(self, N: int, dislikes: [[int]]) -> bool:
        graph = collections.defaultdict(set)
        for u, v in dislikes:
                graph[u].add(v)
                graph[v].add(u)
        degree = collections.defaultdict(int)
        for node, nei in graph.items():
            for i in nei:
                degree[i] += 1

        print(graph)
        print(degree)

        find = False

        while not find:
            temp_length = len(graph)
            for node, degree_ in degree.items():
                if degree_ == 1:
                    degree[degree_] -= 1
                    for n in graph[node]:
                        graph[n].remove(node)
                        if len(graph[n]) == 0:
                            del graph[n]
                        degree[n] -= 1
                    del graph[node]
            if len(graph) == temp_length:
                find = True
            elif len(graph) == 0:
                return True
        return not find




so = Solution()

print(so.possibleBipartition(3, [[1,2],[1,3],[2,4]]))
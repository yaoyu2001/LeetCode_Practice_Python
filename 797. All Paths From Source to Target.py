class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        res = []

        def dfs(cur_node, path):
            if cur_node == target:
                res.append(path)
                return

            for nextNode in graph[cur_node]:
                path.append(nextNode)
                dfs(nextNode, path)
                path.pop()

        path = []
        dfs(0, path)

        return res



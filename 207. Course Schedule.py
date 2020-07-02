# https://www.youtube.com/watch?v=yH4nZe-5wDM&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=7&t=12387s
import collections
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        self.graph = []  # adjacency list indicate graph
        self.visit = []  # Identify a node's visit condition, -1: No visit 0:visiting 1:visited

        for i in range(numCourses):
            self.graph.append(GraphNode(i))
            self.visit.append(-1)

        for item in prerequisites:
            begin = self.graph[item[1]]
            end = self.graph[item[0]]
            begin.neighbors.append(end)

        for i in range(len(self.graph)):
            if self.visit[i] == -1 and not self.DFS_graph(self.graph[i], self.visit):
                return False

        del self.graph

        return True

    def DFS_graph(self, graph_node, visit):

        visit[graph_node.label] = 0
        for item in graph_node.neighbors:
            if visit[item.label] == -1:
                if self.DFS_graph(item, self.visit) == 0:  # Traversal sub nodes
                    return False
            elif visit[item.label] == 0:  # Has loop
                return False

        visit[graph_node.label] = 1  # Finish visit
        return True


# Method 2 topological Sort
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        self.graph = []  # adjacency list indicate graph
        self.degree = []  # A list to save in-degree

        for i in range(numCourses):
            """Build graph, and set all in-degree of nodes to 0"""
            self.graph.append(GraphNode(i))
            self.degree.append(0)

        for item in prerequisites:
            begin = self.graph[item[1]]
            end = self.graph[item[0]]
            begin.neighbors.append(end)
            self.degree[end.label] += 1

        q = collections.deque()

        for item in self.graph:
            if self.degree[item.label] == 0:
                q.append(item)

        while q:
            node = q.popleft()
            for item in node.neighbors:
                self.degree[item.label] -= 1
                if self.degree[item.label] == 0:
                    q.append(item)

        for nums in self.degree:
            if nums == 0: return False

        return True


# From BFS to dijkstra calculate the nearest path in a graph (with weight)
# https://www.youtube.com/watch?v=9wV1VxlfBlI
import heapq
import math


graph = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'C':2,'D':1},
    'C':{'A':1, 'B':2,'D':4,'E':8},
    'D':{'B':1, 'C':4,'E':3,'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6}
}

def init_distance(graph, s):
    distance = {s:0}
    for vertex in graph:
        if vertex !=s:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph,s):
    pqueue = list()
    heapq.heappush(pqueue, (0, s))
    seen = set()

    parent = {s:None} # Find nearest path
    distance = init_distance(graph,s)
    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)  # Once a vertex be taken from a priority queue, mark it as "seen"
        nodes = graph[vertex].keys() # All nodes connected with current vertex
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]: # If a vertex which connected with current "vertex" hasn't seen, calculate the distance
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w)) # Calculate distance, if it less then current distance, replace it.
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent, distance

# print(graph["A"])
parent,distance = dijkstra(graph, "A")
print(parent)
print(distance)
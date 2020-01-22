# https://www.youtube.com/watch?v=bD8RT0ub--0
# Course from Haojie Huang in Youtube
# BSF DSF and find the nearest path
import queue
graph = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D'],
}

def BSF(graph,s):
    queue = list()
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None} # Find nearest path
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        # print(vertex)
    return parent

parent = BSF(graph,"A")
for key in parent:
    print(key, parent[key])
v = 'F'
while v!=None:
    print(v)
    v = parent[v]

def DSF(graph,s):
    stack = list()
    stack.append(s)
    seen = set()
    seen.add(s)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

# DSF(graph,'A')
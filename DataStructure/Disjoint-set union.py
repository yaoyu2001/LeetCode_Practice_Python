# https://www.youtube.com/watch?v=gpmOaSBcbYA


def find_root(x, parent):
    x_root = x
    while parent[x_root] != -1:
        x_root = parent[x_root]
    return x_root


# If return 1 - union successfully, 0 - failed
def union_vertices(x, y, parent, rank):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)
    """If x and y are in the same union, x_root will equal to y_root, in this case, return false"""
    if x_root == y_root:
        return 0
    else:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[y_root] > rank[x_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] +=1
        return 1

def main():
    VERTICES = 6
    parent = [-1] * 6
    rank = [0] * 6
    # edges = [[" " for i in range(2)] for j in range(6)]
    edges = [[0,1],[1,2],[1,3],[3,4],[2,5],[4,5]]
    # print(len(edges))
    for i in range(len(edges)):
        x = edges[i][0]
        y = edges[i][1]
        if union_vertices(x, y, parent,rank) == 0:
            return print("Cycle find")
    return print("No cycles find")



if __name__ == '__main__':

    main()
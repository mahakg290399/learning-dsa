def buildGraph(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if not(node1 in graph): graph[node1] = []
        if not(node2 in graph): graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def hasPath(graph, src, end, visited):
    if src == end: return True
    if src in visited: return False
    visited.add(src)

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, end, visited): return True
    return False

def undirectedGraph(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visitedSet = set()
    return hasPath(graph, nodeA, nodeB, visited=visitedSet)

edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n'],]
# edges = [
#     [4,6],
#     [5,6],
#     [7,6],
#     [8,6],
# ]

print(undirectedGraph(edges, 'i', 'k'))

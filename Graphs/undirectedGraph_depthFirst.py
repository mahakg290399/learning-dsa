def buildGraph(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if not(node1 in graph): graph[node1] = []
        if not(node2 in graph): graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def hasPath(graph, src, end):
    if src == end: return True
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, end): return True
    return False

def undirectedGraph(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB)

edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n'],]

undirectedGraph(edges, 'i', 'j')
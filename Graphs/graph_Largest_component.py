#largest is determined by number of node So more node means the larger graph

def exploreSize(graph, node, visited):
    if node in visited: return 0
    visited.add(node)

    size = 1
    for neighbour in graph[node]:
        size += exploreSize(graph, neighbour, visited)
    return size

def largestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited=visited)
        if longest < size:longest=size
    return longest

graphh={
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4], 
    3:[2,4],
    4:[3,2]
}
print(largestComponent(graphh))
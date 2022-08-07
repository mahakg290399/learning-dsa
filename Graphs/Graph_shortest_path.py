import queue


def graphBuilder(edges):
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if not(node1 in graph): graph[node1] = []
        if not(node2 in graph): graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def shortestPath(graphh,node1,node2):
    queue = [(node1,0)]
    visited = set(node1)
    graph = graphBuilder(edges)
    while len(queue)>0:
        node, dist = queue.pop(0)
        if node == node2: return dist
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
    return -1
        
edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]
graph = graphBuilder(edges)
print(shortestPath(graph, 'w','a'))

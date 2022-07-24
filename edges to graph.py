
#this code will convert the list of edges to a desired graph format
edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
]
#considering thefact that an edge can only have 2 nodes
graph = {}
for edge in edges:
    node1,node2 = edge
    if node1 in graph:
        graph[node1].append(node2)
    if node2 in graph:
        graph[node2].append(node1)  
    if node1 not in graph:
        graph[node1] = [node2]
    if node2 not in graph:
        graph[node2] = [node1]

print(graph)


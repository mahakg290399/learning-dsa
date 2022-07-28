#This code is used to find out the number of disconnected comoponenets. in Other words, it will return number of disconnected subgraphs
def explore(graph, current, visited):
    if(current in visited): return False
    visited.add(current)

    for neighbour in graph[current]:
        explore(graph,neighbour, visited)
    
    return True


def connectedComponenetCount(graph):
    visited = set()
    count = 0
    for node in graph:
        print("Visited: ", visited)
        if explore(graph, node,visited) == True: count+=1 
    return count

graphh = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}
print(connectedComponenetCount(graphh))
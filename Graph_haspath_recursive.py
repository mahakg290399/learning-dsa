#when we have acyclic graph 
def hasPath(graph, src, dst):
    if src == dst:
        return True
    for neighbour in graph[src]:
        if hasPath(graph,neighbour,dst) == True:
            return True
    return False



graphh = {
    'f':['g','h'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

print(hasPath(graphh,'j','h'))
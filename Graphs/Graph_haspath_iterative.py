#when we have acyclic graph
#directed Graph

def hasPath(graph,src,dst):
    queue = [src]
    while len(queue)>0:
        current = queue.pop(0)
        if current == dst: return True
        for neighbour in graph[current]:
            queue.append(neighbour)
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
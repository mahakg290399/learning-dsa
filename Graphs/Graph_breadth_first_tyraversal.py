#itreative
#directed Graph
def breadth(graph, start):
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)

mygraph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
# mygraph = {
#     4 : [6],
#     5 : [6],
#     6 : [4,5,7,8],
#     7 : [6],
#     8 : [6],
# }
breadth(mygraph, 'a')

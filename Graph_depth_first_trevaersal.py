#directed Graph
# def depth(graph0, start):
#     stack = [start]
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#
#         for neighbour in graph0[current]:
#             stack.append(neighbour)

# now using recursion for the same thing
def depth(graphh, start):
    print(start)
    for neighbour in graph[start]:
        depth(graphh, neighbour)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
depth(graph, 'a')

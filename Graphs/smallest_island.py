
import math
def explore(grid, row, column, visited):
    if not((0<=row) and (row<len(grid))):return 0
    if not((0<=column) and (column<len(grid[0]))):return 0
    if grid[row][column] == 'w': return 0
    pos = str(row) + "," + str(column)
    if pos in visited: return 0
    visited.add(pos)
    size =1 
    size += explore(grid, row-1, column, visited)
    size += explore(grid, row+1, column, visited)
    size += explore(grid, row, column-1, visited)
    size += explore(grid, row, column+1, visited)

    return size

def minimumSizedIsland(grid):
    visited = set()
    minSize = math.inf
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            size = explore(grid, row, column, visited)
            if size and (size < minSize): minSize = size
    return minSize
            

grid = [
    ["w","l","w","w","w"],
    ["w","l","w","w","w"],
    ["w","w","w","l","w"],
    ["w","w","l","l","w"],
    ["l","w","w","l","l"],
    ["l","l","w","w","w"]
]

print(minimumSizedIsland(grid))
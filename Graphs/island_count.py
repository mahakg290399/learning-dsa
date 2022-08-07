

def explore(grid , row, column, visited):
    if not((0 <= row) and (row < len(grid))): return False
    if not((0 <= column) and (column < len(grid[0]))): return False
    
    if grid[row][column] == 'w': return False
    pos = str(row)+","+str(column)
    if pos in visited: return False
    visited.add(pos)

    explore(grid, row - 1, column, visited) #moving up
    explore(grid, row + 1, column, visited) #moving down    
    explore(grid, row, column - 1, visited) #moving left
    explore(grid, row, column + 1, visited) #moving right

    return True

def islandCount(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if explore(grid, row, column, visited):
                count += 1
    return count
        

grid = [
    ["w","l","w","w","w"],
    ["w","l","w","w","w"],
    ["w","w","w","l","w"],
    ["w","w","l","l","w"],
    ["l","w","w","l","l"],
    ["l","l","w","w","w"]
]

print(islandCount(grid))
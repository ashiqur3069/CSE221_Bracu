def dfs(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    visited[row][col] = True
    diamonds = 0
    if grid[row][col] == 'D':
        diamonds += 1
    sets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in sets:
        diamonds += dfs(grid, visited, row + x, col + y)

    return diamonds

def max_diamonds(grid):
    max_diamond = 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                max_diamond = max(max_diamond, dfs(grid, visited, i, j))

    return max_diamond

with open("input6.txt", "r") as file:
    n1, n2 = map(int, file.readline().split())
    grid = [file.readline().strip() for i in range(n1)]

max_diamonds_collected = max_diamonds(grid)

with open("output6.txt", "w") as file:
    file.write(str(max_diamonds_collected))
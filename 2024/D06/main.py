from copy import deepcopy

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

grid = []
for line in input:
    grid.append(list(line))

def canMove(r, c):
    return r < len(grid) and r > -1 and c < len(grid[0]) and c > -1

def reach_grid_border(r, c):
    return r == len(grid) - 1 or r == 0 or c == len(grid[0]) - 1 or c == 0

def turnRight(directionIndex):
    return (directionIndex + 1) % 4

def countVisits(new_grid):
    visits = 0
    rows, cols = len(new_grid), len(new_grid[0])
   
    for row in range(rows):
        for col in range(cols):
            if new_grid[row][col] == 'X':
               visits += 1
    
    return visits

def findStartPosition():
    rows, cols = len(grid), len(grid[0])
    r, c = -1, -1
   
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '^':
                r, c = row, col
                break

    return r, c

def scan(new_grid, row, col):         
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    directionIndex = 0
    new_grid[row][col] = 'X'
    r, c = row + directions[directionIndex][0], col + directions[directionIndex][1]
    visted_list = []

    while canMove(r, c):
        if new_grid[r][c] == '.' or new_grid[r][c] == "X":
            new_grid[r][c] = 'X'
            row, col = r, c 
        elif new_grid[r][c] == '#':
            if (r, c, directionIndex) in visted_list:
                return 1
            else:
                visted_list.append((r, c, directionIndex))
            directionIndex = turnRight(directionIndex)
        r, c = row + directions[directionIndex][0], col + directions[directionIndex][1]
    return 0

def solvePartOne(): 
    row, col = findStartPosition()
    new_grid = deepcopy(grid)
    scan(new_grid, row, col)
    return countVisits(new_grid)
                        
def solvePartTwo():
    obstacles = 0
    rows, cols = len(grid), len(grid[0])
    row, col = findStartPosition()

    prev_r, prev_c = 0, 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' or grid[r][c] == 'X':
                grid[prev_r][prev_c] = '.'
                new_grid = grid
                new_grid[r][c] = '#'
                prev_r, prev_c = r, c
                obstacles += scan(new_grid, row, col)

    return obstacles

print(solvePartOne())
print(solvePartTwo())
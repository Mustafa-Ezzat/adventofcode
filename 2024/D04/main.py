with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

grid = []
for item in input:
    grid.append(list(item))

def solvePartOne(): 
    count = 0
    restOfLen = 3
    rows, cols = len(grid), len(grid[0])
    directions = [
        (1, 0),
        (-1, 0), 
        (0, 1), 
        (0, -1),
        (1, 1), 
        (1, -1), 
        (-1, 1), 
        (-1, -1)
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':
                for dir in directions:
                    max_r = row + dir[0] * restOfLen
                    max_c = col + dir[1] * restOfLen
                    if max_r > -1 and max_r < rows and max_c > -1 and max_c < cols:
                        word = "X"
                        for i in range(restOfLen):
                            r = row + dir[0] * (i+1)
                            c = col + dir[1] * (i+1)
                            word += grid[r][c]
                        if word == 'XMAS':
                            count += 1
    return count
                        

def solvePartTwo():
    count = 0
    rows, cols = len(grid), len(grid[0])
    dirs = [
        (1, 1), 
        (-1, -1), 
        (1, -1), 
        (-1, 1)
    ]
    probabilities = [
        'MSMS', 
        'SMSM', 
        'MSSM', 
        'SMMS'
    ]

    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                continue
            if grid[row][col] == 'A':
                word = ""
                for dir in dirs:
                    r, c = row + dir[0], col + dir[1]
                    word += grid[r][c]
                if word in probabilities:
                    count += 1
    return count

print(solvePartOne())
print(solvePartTwo())

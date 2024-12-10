from collections import deque

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def get_grid():
    grid = []
    for line in testCases:
        row = list(line)
        grid.append(row)
    return grid

def get_trailheads(grid):
    rows, cols = len(grid), len(grid[0])
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '0']
    return trailheads

def inside_grid_border(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def strictly_increasing_path(current, neighbor):
    try:
        return int(current) + 1 == int(neighbor)
    except:
        return False

def get_trailhead_score(trailhead, grid, visited):
        stack = [trailhead]
        trailhead_score = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            r, c = stack.pop()
            for x, y in directions:  
                nr, nc = r + x, c + y
                if inside_grid_border(nr, nc, grid) and (nr, nc) not in visited:
                    current, neighbor = grid[r][c], grid[nr][nc]
                    if strictly_increasing_path(current, neighbor):  
                        visited.add((nr, nc))
                        stack.append((nr, nc))
                        if grid[nr][nc] == '9':
                            trailhead_score += 1
        return trailhead_score

def calculate_trailhead_scores(grid):
    trailheads = get_trailheads(grid)
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        visited.add(trailhead)
        trailhead_score = get_trailhead_score(trailhead, grid, visited)
        total_score += trailhead_score
    
    return total_score

def solve_part_one():
    grid = get_grid()
    result = calculate_trailhead_scores(grid)
    return result

print(solve_part_one())
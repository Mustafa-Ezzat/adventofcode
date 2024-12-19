import heapq
from copy import deepcopy

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def init_space_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append('.')
        grid.append(row)
    return grid

def get_corrupted_coordinates():
    coordinates = []
    for line in input:
        x, y = map(int, list(line.split(',')))
        coordinates.append((x, y))
    return coordinates

def get_grid(grid, bytes):
    coordinates = get_corrupted_coordinates()
    while bytes > 0:
        x, y = coordinates[bytes - 1]
        grid[y][x] = '#' 
        bytes -= 1
    return grid

def in_grid_bound(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols  

def get_maze_start_and_end(grid):
    rows, cols = len(grid), len(grid[0])
    start, end = (0, 0), (rows - 1, cols - 1) 
    return start, end

def lowest_path_score(grid):
    start, end = get_maze_start_and_end(grid)   
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Dijkstra's algorithm: priority queue
    # (cost, x, y, last_direction)
    queue = [(0, start[0], start[1], -1)]    
    visited = set()
    
    while queue:
        cost, x, y, last_direction = heapq.heappop(queue)
        
        if (x, y) == end: return cost
        
        state = (x, y, last_direction)
        if state in visited:
            continue
        visited.add(state)
        
        for index, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            if in_grid_bound(grid, new_y, new_x) and grid[new_y][new_x] != '#':
                step_cost = 1                
                heapq.heappush(queue, (cost + step_cost, new_x, new_y, index))
    
    return -1

def solve_part_one():
    rows, cols = 71, 71
    grid = init_space_grid(rows, cols)
    grid = get_grid(grid, 1024)
    lowest_score = lowest_path_score(grid)
    return lowest_score

def solve_part_two():
    low, high = 0, len(input)
    mid = low + high // 2
    rows, cols = 71, 71
    grid = init_space_grid(rows, cols)
    first_block = high

    while low <= high:
        new_grid = deepcopy(grid)
        new_grid = get_grid(new_grid, mid)
        lowest_score = lowest_path_score(new_grid)
        if lowest_score != -1:
            low =  mid + 1
            mid = (low + high) // 2
        else:            
            if mid < first_block:
                first_block = mid
            else:
                break
            high =  mid - 1
            mid = (low + high) // 2
                    
    coordinates = get_corrupted_coordinates()
    return coordinates[first_block - 1]

print(solve_part_one())
print(solve_part_two())
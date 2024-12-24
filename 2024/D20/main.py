import heapq
from copy import deepcopy

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def get_maze():
    maze = [] 
    for line in testCases:
        maze.append(line)
    return maze

def get_maze_start_and_end(maze):
    start = end = None
    for y, row in enumerate(maze):
        if 'S' in row:
            start = (row.index('S'), y)
        if 'E' in row:
            end = (row.index('E'), y)
        if start and end:
            break
    return start, end

def in_grid_bound(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols 

def lowest_path_score(maze):
    start, end = get_maze_start_and_end(maze)   
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Dijkstra's algorithm: priority queue
    # (cost, x, y, last_direction)
    queue = [(0, start[0], start[1])]    
    visited = set()
    
    while queue:
        cost, x, y = heapq.heappop(queue)
        
        if (x, y) == end: return cost
        
        state = (x, y)
        if state in visited:
            continue
        visited.add(state)
        
        for (dx, dy) in directions:
            new_x, new_y = x + dx, y + dy
            
            if in_grid_bound(maze, new_y, new_x) and maze[new_y][new_x] != '#':
                step_cost = 1                
                heapq.heappush(queue, (cost + step_cost, new_x, new_y))
    
    return -1

def solve_part_one():
    maze = get_maze()
    rows, cols = len(maze), len(maze[0])
    lowest_score = lowest_path_score(maze)
    cheats = 0
    for r in range(rows):
        for c in range(cols):
            new_maze = [list(row) for row in maze]
            if new_maze[r][c] != '#':
                continue
            new_maze[r][c] = '.'
            new_lowest_score = lowest_path_score(new_maze)
            if new_lowest_score <= lowest_score - 60:
                cheats += 1 
    return cheats

print(solve_part_one())
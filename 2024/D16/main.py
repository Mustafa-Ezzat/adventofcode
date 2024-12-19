import heapq

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def get_maze():
    maze = [] 
    for line in input:
        maze.append(line)
    return maze

def lowest_path_score(maze):

    rows, cols = len(maze), len(maze[0])
    start, end = (rows - 2, 1), (1, cols - 2)    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Dijkstra's algorithm: priority queue
    # (cost, x, y, last_direction)
    pq = [(0, start[0], start[1], -1)]    
    visited = set()
    
    while pq:
        cost, x, y, last_direction = heapq.heappop(pq)
        
        if (x, y) == end:
            return cost
        
        state = (x, y, last_direction)
        if state in visited:
            continue
        visited.add(state)
        
        for index, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            if maze[new_y][new_x] != '#':
                step_cost = 1001 if (last_direction != -1 and last_direction != index) else 1                
                heapq.heappush(pq, (cost + step_cost, new_x, new_y, index))
    
    return -1

def draw_intersection_best_paths(maze, best_paths):
    rows, cols = len(maze), len(maze[0])
    start, end = (rows - 2, 1), (1, cols - 2) 
    path_maze = [list(row) for row in maze]
    
    for best_path in best_paths:
        for x, y in best_path:
            if path_maze[y][x] == '.':
                path_maze[y][x] = 'O'
    path_maze[start[0]][start[1]] = 'O'
    path_maze[end[0]][end[1]] = 'O'
    return path_maze

def scan_all_best_paths(maze):
    
    rows, cols = len(maze), len(maze[0])
    start, end = (rows - 2, 1), (1, cols - 2)    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Dijkstra's algorithm: priority queue
    # (cost, x, y, last_direction, path)
    pq = [(0, start[0], start[1], -1, [start])]    
    visited = {}
    best_paths = []
    lowest_cost = float('inf')
    
    while pq:
        cost, x, y, last_direction, path = heapq.heappop(pq)
        
        current_state = (x, y, last_direction)
        if current_state in visited and visited[current_state] < cost:
            continue
        
        if (x, y) == end:
            if cost < lowest_cost:
                lowest_cost = cost
                best_paths = [path]
            elif cost == lowest_cost:
                best_paths.append(path)
            continue
        
        visited[current_state] = cost
        
        for direction_idx, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            if maze[new_y][new_x] != '#':
                new_cost = 1001 if (last_direction != -1 and last_direction != direction_idx) else 1
                new_path = path + [(new_x, new_y)]
                heapq.heappush(pq, (cost + new_cost, new_x, new_y, direction_idx, new_path))
    
    if not best_paths:
        return []
        
    return best_paths

def solve_part_one():
    maze = get_maze()
    lowest_score = lowest_path_score(maze)
    return lowest_score

def solve_part_two():
    maze = get_maze()
    best_paths = scan_all_best_paths(maze)
    path_maze = draw_intersection_best_paths(maze, best_paths)
    rows, cols = len(path_maze), len(path_maze[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if path_maze[r][c] == 'O':
                result += 1
    return result

print(solve_part_one())
print(solve_part_two())

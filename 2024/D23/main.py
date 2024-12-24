from collections import defaultdict

with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def get_connections():
    return input

def get_three_connected(connections):
    graph = defaultdict(set)
    for pair in connections:
        a, b = pair.split('-')
        graph[a].add(b)
        graph[b].add(a)
    
    result = set()
    nodes = graph.keys()
    
    for node1 in nodes:
        for node2 in graph[node1]:
            if node2 <= node1: continue
            for node3 in graph[node2]:
                if node3 <= node2: continue
                if node3 in graph[node1]:
                    result.add((node1, node2, node3))
    
    return result

def solve_part_one():
    sum = 0
    connections = get_connections()
    three_connected = get_three_connected(connections)
    for c1, c2, c3 in three_connected:
        if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
            sum += 1
    
    return sum

print(solve_part_one())
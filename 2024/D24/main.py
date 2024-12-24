with open("testCases.txt", "r") as f:
    testCases = f.read()

with open("input.txt", "r") as f:
    input = f.read()

def get_values_and_operations():
    values, operations = input.split('\n\n')
    map = {}
    for line in values.splitlines():
        key, val = line.split(': ')
        map[key] = int(val)
    return map, operations.splitlines()


def get_gate_value(map, operation):
        left, gate, right, _, _ = operation.split()
        left_val, right_val = map[left], map[right]
        result = 0
        match gate:
            case 'AND':
                result = int(left_val and right_val)
            case 'OR':
                result = int(left_val or right_val)
            case 'XOR':  
                result = int(left_val != right_val)
        
        return result

def get_final_map(map, operations):
    while operations:
        in_map = []
        
        for operation in operations:
            left, _, right, _, result = operation.split()
            if left in map and right in map:
                map[result] = get_gate_value(map, operation)
                in_map.append(operation)
        
        for operation in in_map:
            operations.remove(operation)
        
    return map

def solve_part_one():
    sum = 0
    map, operations = get_values_and_operations()
    map = get_final_map(map, operations)
    target_keys = [key for key in map if key [0] == 'z']
    for index, key in enumerate(sorted(target_keys)): 
        sum += pow(2, index) * map[key]
        
    return sum

print(solve_part_one())
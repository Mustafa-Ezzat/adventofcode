with open("testCases.txt", "r") as f:
    testCases = f.read().splitlines()

with open("input.txt", "r") as f:
    input = f.read().splitlines()

def prepare_data():
    list = []
    for line in input:
        line = line.split(': ')
        test_value = int(line[0]) 
        numbers = []
        for item in line[1].split(' '):
            numbers.append(int(item))
        list.append((test_value, numbers))
    
    return list

def find_combinations(numbers, target): 
    stack = [(0, 0)] 
    while stack: 
        index, current_value = stack.pop()
        if index == len(numbers): 
            if current_value == target:
                return target
        else:
            stack.append((index + 1, current_value + numbers[index])) 
            stack.append((index + 1, current_value * numbers[index])) 
    return 0

def find_combinations_two(numbers, target): 
    stack = [(0, 0)] 
    while stack: 
        index, current_value = stack.pop()
        if index == len(numbers): 
            if current_value == target:
                return target
        else:
            stack.append((index + 1, current_value + numbers[index])) 
            stack.append((index + 1, current_value * numbers[index])) 
            concat = str(current_value) + str(numbers[index])
            stack.append((index + 1, int(concat))) 
    return 0
        
def solve_part_one():
    result = 0
    items = prepare_data()
    for item in items:
        test_value, numbers = item[0], item[1]
        result += find_combinations(numbers, test_value)
    
    return result

def solve_part_two():
    result = 0
    items = prepare_data()
    for item in items:
        test_value, numbers = item[0], item[1]
        result += find_combinations_two(numbers, test_value)
    
    return result

print(solve_part_one())
print(solve_part_two())
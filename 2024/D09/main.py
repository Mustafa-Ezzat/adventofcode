with open("testCases.txt", "r") as f:
    testCases = f.read().strip()

with open("input.txt", "r") as f:
    input = f.read().strip()

def prepare_data():
    data = list(map(int, input))
    id = 0
    block_list = []
    for i in range(len(data)):
        item = data[i]
        if item == 0:
            continue
        if i % 2 == 0:
            block_list += [str(id)] * item
            id += 1
        else:
            block_list += ['.'] * item
    return block_list
        
def check_sum(disk):
    sum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        sum += int(disk[i]) * i
    
    return sum

def find_file_span(disk, file_id):
    start = disk.index(file_id)
    end = len(disk)
    for i in range(start + 1, end):
        if disk[i] != file_id:
            end = i
            break

    return start, end - 1

def find_leftmost_space(disk, size):
    free_start = None
    free_count = 0
    for i, block in enumerate(disk):
        if block == '.':
            if free_start is None:
                free_start = i
            free_count += 1
            if free_count == size:
                return free_start
        else:
            free_start = None
            free_count = 0
    return None

def move_file(disk, file_id, start, end, target_start):
    size = end - start + 1
    for i in range(start, end + 1):
        disk[i] = '.'
    for i in range(size):
        disk[target_start + i] = file_id

def relocate_files(disk):
    file_ids = get_file_ids(disk)
    for file_id in file_ids:
        start, end = find_file_span(disk, file_id)
        size = end - start + 1
        target_start = find_leftmost_space(disk, size)
        if target_start is not None and target_start < start:
            move_file(disk, file_id, start, end, target_start)

    return disk

def get_file_ids(input_list):
    return list(map(str, sorted(list(map(int, set([item for item in input_list if item != '.']))), reverse=True)))

def solve_part_one():
    disk = prepare_data()
    i, j = 1, len(disk) - 1
    while j > i:
        if disk[i] != '.':
            i += 1
        if disk[j] == '.':
            j -= 1
        elif disk[i] == '.' and disk[j] != '.':
            disk[i], disk[j] = disk[j], disk[i]
            i += 1
            j -= 1
    return check_sum(disk[:i+1])

def solve_part_two():
    disk = prepare_data()
    disk = relocate_files(disk)
    return check_sum(disk)

print(solve_part_one())
print(solve_part_two())
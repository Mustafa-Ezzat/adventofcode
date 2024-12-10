with open("testCases.txt", "r") as f:
    testCases = f.read().strip()

with open("input.txt", "r") as f:
    input = f.read().strip()

def init_disk():
    data = list(map(int, input))
    id = 0
    disk = []
    for i in range(len(data)):
        item = data[i]
        if item == 0:
            continue
        if i % 2 == 0:
            disk += [str(id)] * item
            id += 1
        else:
            disk += ['.'] * item
    return disk
        
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

    return start, end

def find_left_most_space(disk, size):
    first_dot = None
    dots = 0
    for i, block in enumerate(disk):
        if block == '.':
            if first_dot is None:
                first_dot = i
            dots += 1
            if dots == size:
                break
        else:
            first_dot = None
            dots = 0
    return first_dot

def relocate_file(disk, file_id, start, end, target_start):
    size = end - start
    for i in range(start, end):
        disk[i] = '.'
    for i in range(size):
        disk[target_start + i] = file_id

def unique_file_ids(input_list):
    return list(map(str, sorted(list(map(int, set([item for item in input_list if item != '.']))), reverse=True)))

def relocate_files(disk):
    file_ids = unique_file_ids(disk)
    for file_id in file_ids:
        start, end = find_file_span(disk, file_id)
        size = end - start
        target_start = find_left_most_space(disk, size)
        if target_start is not None and target_start < start:
            relocate_file(disk, file_id, start, end, target_start)

    return disk

def solve_part_one():
    disk = init_disk()
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
    disk = init_disk()
    disk = relocate_files(disk)
    return check_sum(disk)

print(solve_part_one())
print(solve_part_two())
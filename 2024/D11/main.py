with open("testCases.txt", "r") as f:
    testCases = f.read()

with open("input.txt", "r") as f:
    input = f.read()

def get_stones():
    stones = list(map(int, input.split(' '))) 
    return stones

def is_even_digits(stone):
    return len(str(stone)) % 2 == 0

def divide(stone):
    digits = str(stone)
    mid = len(digits) // 2
    left, right = int(digits[:mid]), int(digits[mid:])
    return left, right

def reengraving_stones(stones, blinks):
    memo = {} 

    def break_down_stone(stone, remaining_blinks):
        if remaining_blinks == 0:
            return 1 
         
        if (stone, remaining_blinks) in memo:
            return memo[(stone, remaining_blinks)]
        
        if stone == 0:
            result = break_down_stone(1, remaining_blinks - 1)
        elif is_even_digits(stone):
            left, right = divide(stone)
            left_process = break_down_stone(left, remaining_blinks - 1)
            right_process = break_down_stone(right, remaining_blinks - 1)
            result = left_process + right_process
        else:
            new_stone = stone * 2024
            result = break_down_stone(new_stone, remaining_blinks - 1)
        
        memo[(stone, remaining_blinks)] = result
        return result

    final_stones = 0
    for stone in stones:
        final_stones += break_down_stone(stone, blinks)
    
    return final_stones

def get_number_of_stones_after(blinks):
    stones = get_stones()
    result = reengraving_stones(stones, blinks)
    return result

def solve_part_one():
    return get_number_of_stones_after(25)
    
def solve_part_two():
    return get_number_of_stones_after(75)

print(solve_part_one())
print(solve_part_two())

import re

with open("testCases.txt", "r") as f:
    testCases = f.read()

with open("input.txt", "r") as f:
    input = f.read()

def solvePartOne(input):
    total = 0
    
    regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    result = regex.findall(input)
    for item in result:
        regex = re.compile(r'\d{1,3}')
        result = regex.findall(item)
        total += int(result[0]) * int(result[1])
    return total

def solvePartTwo():
    total = 0
    regex = re.compile(r'don\'t\(\)')
    dontList = regex.split(input)
    total += solvePartOne(dontList.pop(0))
    for item in dontList:
        regex = re.compile(r'do\(\)')
        doList = regex.split(item)
        doList.pop(0)
        total += solvePartOne(str(doList))

    return total

print(solvePartOne(input))
print(solvePartTwo())
with open("testCases.txt", "r") as f:
    testCases = f.read().split("\n\n")

with open("input.txt", "r") as f:
    input = f.read().split('\n\n')

rules = input[0].split('\n')
updates = input[1].split('\n')
updateList = []
for update in updates:
    updateList.append(update.split(','))

def countCorrect(update, is_valid):
    count = 0
    if is_valid:
            middle = int(len(update) / 2)
            item = int(update[middle])
            count += item
    return count

def solvePartOne(): 
    total = 0
    for update in updateList:
        is_valid = True
        for i in range(len(update)):
            rule = ""
            for j in range(i, len(update)):
                if i == j:
                    continue
                rule = update[i] + "|" + update[j]
                if rule in rules:
                    continue
                else:
                    is_valid = False
                    break
        total += countCorrect(update, is_valid)

    return total
                        
def solvePartTwo():
    total = 0
    for update in updateList:
        is_valid = True
        for i in range(len(update)):
            rule = ""
            for j in range(i, len(update)):
                if i == j:
                    continue
                rule = update[i] + "|" + update[j]
                reversed_rule = update[j] + "|" + update[i]
                if rule in rules:
                    continue
                elif reversed_rule in rules:
                    update[i], update[j] = update[j], update[i]
                    continue
                else:
                    is_valid = False
                    break
        total += countCorrect(update, is_valid)

    return total

val1 = solvePartOne()
print(val1)
val2 = solvePartTwo() 
print(val2 - val1)

import Foundation

let file = "linput.txt"

func isAscending(_ list: [Int]) -> Bool {
	return list == list.sorted() && Set(list).count == list.count
}

func isDescending(_ list: [Int]) -> Bool {
	return list == list.sorted(by: >) && Set(list).count == list.count
}

func readTestCases(_ file: String) -> [[Int]] {
	guard let testCases = try? NSString(contentsOfFile: file, encoding: String.Encoding.utf8.rawValue) else {
		return []
	}
	
	let lines = testCases
		.lowercased
		.split(separator: "\n")
		.map { String($0) }
	
	return split(lines)
}

func split(_ lines: [String]) -> [[Int]] {
	var lists: [[Int]] = []
	
	for line in lines {
		let list = line
			.split(separator: " ")
			.compactMap { Int($0) }

		lists.append(list)
	}
	
	return lists
}

func unsafe(_ list: [Int]) -> Int {
	guard list.count > 1 else { return 0 }
	
	guard isAscending(list) || isDescending(list) else {
		return 1
	}
	
	var p1 = 0
	var p2 = 1
	var sign = 1
	var delta = list[p1] - list[p2]
	
	if delta < 0 {
		sign = -1
	}
	
	while p2 < list.count {
		delta = sign * (list[p1] - list[p2])
		if delta > 3 || delta < 1 {
			return 1
		}
		else {
			p1 += 1
			p2 += 1
		}
	}
	
	return 0
}

func solvePartOne() -> Int {
	var unsafeCount = 0
	let lists = readTestCases(file)
	guard lists.count > 0 else { return 0 }
	
	for list in lists {
		unsafeCount += unsafe(list)
	}
	
	return lists.count - unsafeCount
}

func solvePartTwo() -> Int {
	var unsafeCount = 0
	let lists = readTestCases(file)
	guard lists.count > 0 else { return 0 }
	
	for list in lists {
		var index = 0
		var unsafeCheck = 0
		while index < list.count {
			var dampenerList = list
			dampenerList.remove(at: index)
			unsafeCheck = unsafe(dampenerList)
			index += 1
			if unsafeCheck == 0 {
				break
			}
			else {
				continue
			}
		}
		unsafeCount += unsafeCheck
	}
	
	return lists.count - unsafeCount
}

print(solvePartOne())
print(solvePartTwo())
l

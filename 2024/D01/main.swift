//
//  main.swift
//  p01
//
//  Created by Mustafa Ezzat on 12/2/24.
//

import Foundation

let file = "input.txt"

func readTestCases(_ file: String) -> (left: [Int], right: [Int]) {
	guard let testCases = try? NSString(contentsOfFile: file, encoding: String.Encoding.utf8.rawValue) else {
		return ([], [])
	}
	
	let lines = testCases
		.lowercased
		.split(separator: "\n")
		.map { String($0) }
	
	return split(lines)
}

func split(_ lines: [String]) -> (left: [Int], right: [Int]) {
	var left: [Int] = []
	var right: [Int] = []
	
	for line in lines {
		let pair = line.split(separator: " ")
		left.append(Int(pair[0]) ?? -1)
		right.append(Int(pair[1]) ?? -1)
	}
	
	return (left, right)
}

func solvePartOne() -> Int {
	var total = 0
	let tuple = readTestCases(file)
	let left = tuple.left.sorted()
	let right = tuple.right.sorted()
	
	for i in 0..<left.count {
		total += abs(left[i] - right[i])
	}
	
	return total
}

func solvePartTwo() -> Int {
	var score = 0
	let tuple = readTestCases(file)
	var counts: [Int: Int] = [:]
	
	for item in tuple.right {
		counts[item] = (counts[item] ?? 0) + 1
	}
	
	for item in tuple.left {
		score += item * (counts[item] ?? 0)
	}
	
	return score
}

print(solvePartOne())
print(solvePartTwo())

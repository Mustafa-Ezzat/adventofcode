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
	
	let pairs = testCases
		.lowercased
		.split(separator: "\n")
		.map { String($0) }
	
	return split(pairs)
}

func split(_ pairs: [String]) -> (left: [Int], right: [Int]) {
	var left: [Int] = []
	var right: [Int] = []
	
	for pair in pairs {
		let sides = pair.split(separator: " ")
		left.append(Int(sides[0]) ?? -1)
		right.append(Int(sides[1]) ?? -1)
	}
	
	return (left, right)
}

func solvePartOne() -> Int {
	var totalDistance = 0
	let tuple = readTestCases(file)
	let left = tuple.left.sorted()
	let right = tuple.right.sorted()
	
	for i in 0..<left.count {
		totalDistance += abs(left[i] - right[i])
	}
	
	return totalDistance
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

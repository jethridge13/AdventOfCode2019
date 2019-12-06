import unittest
import sys

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def parseInstruction(ins):
	direction = ins[0]
	length = int(ins[1:])
	return (direction, length)

def generateLineSegments(line):
	segments = []
	curIndex = [0, 0]
	instructions = line.split(',')
	while len(instructions) > 0:
		# Get starting point for line
		start = curIndex.copy()
		# Determine ending point for line
		ins = parseInstruction(instructions.pop(0))
		if ins[0] == 'R':
			curIndex[0] += ins[1]
		elif ins[0] == 'L':
			curIndex[0] -= ins[1]
		elif ins[0] == 'U':
			curIndex[1] += ins[1]
		elif ins[0] == 'D':
			curIndex[1] -= ins[1]
		end = curIndex.copy()
		segments.append((start, end))
	return segments

def checkForIntersection(line1, line2):
	# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
	result = (False, [])

	line1pt1 = line1[0]
	line1pt2 = line1[1]
	line2pt1 = line2[0]
	line2pt2 = line2[1]

	o1 = getOrientation(line1pt1, line1pt2, line2pt1)
	o2 = getOrientation(line1pt1, line1pt2, line2pt2)
	o3 = getOrientation(line2pt1, line2pt2, line1pt1)
	o4 = getOrientation(line2pt1, line2pt2, line1pt2)

	if (o1 != o2 and o3 != o4):
		intersect = getIntersect(line1pt1, line1pt2, line2pt1, line2pt2)
		return (True, intersect)
	return result

def getOrientation(pt1, pt2, pt3):
	# https://www.geeksforgeeks.org/orientation-3-ordered-points/
	# 0 - collinear
	# 1 - clockwise
	# 2 - counterclockwise
	val = (pt2[1] - pt1[1]) * (pt3[0] - pt2[0]) - \
		(pt2[0] - pt1[0]) * (pt3[1] - pt2[1])
	if val == 0:
		return 0
	if val > 0:
		return 1
	return 2

def getIntersect(pt1, pt2, pt3, pt4):
	# https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/
	# a1x + b1y = c1
	a1 = pt2[1] - pt1[1]
	b1 = pt1[0] - pt2[0]
	c1 = a1 * (pt1[0]) + b1 * (pt1[1])
	# a2x + b2y = c2
	a2 = pt4[1] - pt3[1]
	b2 = pt3[0] - pt4[0]
	c2 = a2 * (pt3[0]) + b2 * (pt3[1])

	determinant = a1 * b2 - a2 * b1

	if determinant == 0:
		raise('Parallel')

	x = (b2 * c1 - b1 * c2) / determinant
	y = (a1 * c2 - a2 * c1) / determinant

	return [x, y]

def getManhattanDistance(pt1, pt2):
	return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def part1():
	data = load('Day3.txt')
	data = data.split()
	line1 = data[0]
	line2 = data[1]
	line1Segments = generateLineSegments(line1)
	line2Segments = generateLineSegments(line2)
	closestIntersectionDistance = sys.maxsize
	start = [0,0]
	for i in line1Segments:
		for j in line2Segments:
			result = checkForIntersection(i, j)
			if result[0]:
				distance = getManhattanDistance(start, result[1])
				closestIntersectionDistance = min(closestIntersectionDistance, distance)
	return closestIntersectionDistance				


class TestDay3(unittest.TestCase):

	def test1(self):
		self.assertEqual(parseInstruction('U13'), ('U', 13))

	def test2(self):
		self.assertEqual(parseInstruction('R9999'), ('R', 9999))

	def test3(self):
		self.assertEqual(generateLineSegments('R75'), [([0,0],[75,0])])

	def test4(self):
		inp = 'R75,D30'
		outp = [([0,0], [75,0]), ([75,0], [75,-30])]
		self.assertEqual(generateLineSegments(inp), outp)

	def test5(self):
		pt1 = [0,0]
		pt2 = [4,4]
		pt3 = [1,1]
		self.assertEqual(getOrientation(pt1, pt2, pt3), 0)

	def test6(self):
		pt1 = [0,0]
		pt2 = [4,4]
		pt3 = [8,2]
		self.assertEqual(getOrientation(pt1, pt2, pt3), 1)
	
	def test7(self):
		pt1 = [0,0]
		pt2 = [4,4]
		pt3 = [1,2]
		self.assertEqual(getOrientation(pt1, pt2, pt3), 2)

	def test8(self):
		line1 = [[0,0],[1,1]]
		line2 = [[5,5],[8,8]]
		result = checkForIntersection(line1, line2)
		self.assertFalse(result[0])

	def test9(self):
		line1 = [[0,0],[5,5]]
		line2 = [[0,6], [6,0]]
		result = checkForIntersection(line1, line2)
		self.assertTrue(result[0])
		self.assertEqual(result[1], [3,3])

	def test10(self):
		pt1 = [0,0]
		pt2 = [1,1]
		result = getManhattanDistance(pt1, pt2)
		self.assertEqual(result, 2)

	def test11(self):
		pt1 = [0.0,0.0]
		pt2 = [1.0,1.0]
		result = getManhattanDistance(pt1, pt2)
		self.assertEqual(result, 2)
	
if __name__ == '__main__':
	# unittest.main()
	# Part 1: 855
	print(part1())

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

def part2(data=None):
	if not data:
		data = load('Day3.txt')
	data = data.split()
	line1 = data[0]
	line2 = data[1]
	line1Segments = generateLineSegments(line1)
	line2Segments = generateLineSegments(line2)
	intersections = []
	closestIntersectionSteps = sys.maxsize
	line1Steps = 0
	lastLine1Pt = [0,0]
	lastLine2Pt = [0,0]
	for i in line1Segments:
		line2Steps = 0
		for j in line2Segments:
			result = checkForIntersection(i, j)
			if result[0] and result[1] != [0.0, 0.0]:
				# Intersection: Calculate size
				line1StepsFromLastPt = getManhattanDistance(lastLine1Pt, result[1])
				line2StepsFromLastPt = getManhattanDistance(lastLine2Pt, result[1])
				steps = line1Steps + line2Steps + line1StepsFromLastPt + line2StepsFromLastPt
				closestIntersectionSteps = min(closestIntersectionSteps, steps)
				print('Intersection at %s. Steps in line 1: %s+%s. Steps in line 2: %s+%s. Total steps: %s' % (result[1], line1Steps, line1StepsFromLastPt, line2Steps, line2StepsFromLastPt, steps))
			line2Steps += getManhattanDistance(lastLine2Pt, j[1])
			print('Adding to line2Steps: %s. Total: %s' % (getManhattanDistance(lastLine2Pt, j[1]), line2Steps))
			lastLine2Pt = j[1]
		# Because there are no diagonal lines, we can use
		# the Manhattan distance to get number of steps
		line1Steps += getManhattanDistance(lastLine1Pt, i[1])
		lastLine1Pt = i[1]
	return int(closestIntersectionSteps)

class TestDay3(unittest.TestCase):

	# Part 1 Tests
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

	# Part 2 Tests
	def test12(self):
		inp = 'R8,U5,L5,D3\n' + \
				'U7,R6,D4,L4'
		outp = 30
		self.assertEqual(part2(inp), outp)

	'''
	def test13(self):
		inp = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\n' + \
				'U62,R66,U55,R34,D71,R55,D58,R83'
		outp = 610
		self.assertEqual(part2(inp), outp)

	def test14(self):
		inp = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n' + \
				'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
		outp = 410
		self.assertEqual(part2(inp), outp)
	'''
	
if __name__ == '__main__':
	unittest.main()
	# Part 1: 855
	print(part1())
	# Part 2: 885418 too high
	# 22852 too high
	print(part2())
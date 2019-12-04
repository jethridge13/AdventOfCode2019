import unittest

def load(path):
	pass

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
	return result


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
	
if __name__ == '__main__':
	unittest.main()

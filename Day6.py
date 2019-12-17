import unittest

class Node(object):

	def __init__(self, name, root=None, children=[]):
		self.name = name
		self.root = root
		self.children = []

	def __str__(self):
		return '%s, root: %s, children: %s' % (self.name, self.root, len(self.children))

	def getTotalLeaves(self, orbits=0):
		if len(self.children) == 0:
			return orbits
		count = 0
		for child in self.children:
			count += child.getTotalLeaves(orbits+1)
		return count + orbits

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def parseLine(line):
	return line.split(')')

def part1(data=None):
	if not data:
		data = load('Day6.txt')
	lines = data.split()
	nodeMap = {}
	# Build node tree
	for line in lines:
		line = parseLine(line)
		planetName = line[0]
		satelliteName = line[1]
		planet = nodeMap.get(planetName, Node(planetName))
		satellite = nodeMap.get(satelliteName, Node(satelliteName))
		planet.children.append(satellite)
		satellite.root = planet
		nodeMap[planetName] = planet
		nodeMap[satelliteName] = satellite
	com = nodeMap.get('COM')
	return com.getTotalLeaves()

def part2():
	pass

class TestDay5(unittest.TestCase):

	def test1(self):
		inp = 'COM)B'
		outp = parseLine(inp)
		self.assertEqual(outp[0], 'COM')
		self.assertEqual(outp[1], 'B')

	def test2(self):
		inp = 'WR4)TZN'
		outp = parseLine(inp)
		self.assertEqual(outp[0], 'WR4')
		self.assertEqual(outp[1], 'TZN')

	def test3(self):
		inp = 'COM)B\n' + \
				'B)C\n' + \
				'C)D\n' + \
				'D)E\n' + \
				'E)F\n' + \
				'B)G\n' + \
				'G)H\n' + \
				'D)I\n' + \
				'E)J\n' + \
				'J)K\n' + \
				'K)L'
		outp = 42
		self.assertEqual(part1(inp), outp)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 160040
	print(part1())
	# Part 2: 
	print(part2())
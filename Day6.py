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

	def findChild(self, name):
		if self.name == name:
			return 0
		if len(self.children) == 0:
			return -1
		for child in self.children:
			count = child.findChild(name)
			if count > -1:
				return count + 1
		return -1

	def findOtherNode(self, name, path=[]):
		if self.name == name:
			return path + [self.name]
		if len(self.children) == 0:
			return self.root.findOtherNode(name, path+[self.name])
		for child in self.children:
			if child.findChild(name) > -1:
				return child.findOtherNode(name, path+[self.name])
		return self.root.findOtherNode(name, path+[self.name])

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def parseLine(line):
	return line.split(')')

def buildTree(lines):
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
	return nodeMap

def part1(data=None):
	if not data:
		data = load('Day6.txt')
	lines = data.split()
	nodeMap = buildTree(lines)
	com = nodeMap.get('COM')
	return com.getTotalLeaves()

def part2(data=None):
	if not data:
		data = load('Day6.txt')
	lines = data.split()
	nodeMap = buildTree(lines)
	you = nodeMap.get('YOU')
	path = you.findOtherNode('SAN')
	# Due to how the path is found,
	# Substract starting node, ending node, and beginning orbitting node
	return len(path) - 3

class TestDay6(unittest.TestCase):

	# Part 1 tests
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

	# Part 2 tests
	def test4(self):
		root = Node('COM')
		child = Node('CHILD', root=root)
		root.children.append(child)
		self.assertEqual(root.findChild('CHILD'), 1)

	def test5(self):
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
				'K)L\n' + \
				'K)YOU\n' + \
				'I)SAN'
		outp = 4
		self.assertEqual(part2(inp), 4)

if __name__ == '__main__':
	# unittest.main()
	# Part 1: 160040
	print(part1())
	# Part 2: 373
	print(part2())
import unittest
import sys

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def breakIntoLayers(data, width, height):
	n = width * height
	return [data[i:i+n] for i in range(0, len(data), n)]

def part1():
	data = load('Day8.txt')
	layers = breakIntoLayers(data, 25, 6)
	layerIndex = 0
	zeroCount = sys.maxsize
	for index, layer in enumerate(layers):
		layerZeroCount = layer.count('0')
		if layerZeroCount < zeroCount:
			layerIndex = index
			zeroCount = layerZeroCount
	return layers[layerIndex].count('1') * layers[layerIndex].count('2')

def part2():
	pass

class TestDay8(unittest.TestCase):

	# Part 1 tests
	def test1(self):
		width = 3
		height = 2
		layers = breakIntoLayers('123456789012', width, height)
		self.assertEqual(layers[0], '123456')
		self.assertEqual(layers[1], '789012')

if __name__ == '__main__':
	# unittest.main()
	# Part 1: 2318
	print(part1())
	# Part 2: 
	print(part2())
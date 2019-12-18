import unittest
import sys

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def breakIntoLayers(data, chunk):
	return [data[i:i+chunk] for i in range(0, len(data), chunk)]

def condenseLayers(layers):
	# Assuming all layers are same length as first layer
	pixels = len(layers[0])
	result = ''
	for i in range(pixels):
		for layer in layers:
			if layer[i] != '2':
				result += layer[i]
				break
	return result

def printLayer(layer, width):
	layers = breakIntoLayers(layer, width)
	for layer in layers:
		layer = layer.replace('0', ' ')
		print(layer)

def part1():
	data = load('Day8.txt')
	layers = breakIntoLayers(data, 25 * 6)
	layerIndex = 0
	zeroCount = sys.maxsize
	for index, layer in enumerate(layers):
		layerZeroCount = layer.count('0')
		if layerZeroCount < zeroCount:
			layerIndex = index
			zeroCount = layerZeroCount
	return layers[layerIndex].count('1') * layers[layerIndex].count('2')

def part2():
	data = load('Day8.txt')
	layers = breakIntoLayers(data, 25 * 6)
	result = condenseLayers(layers)
	printLayer(result, 25)

class TestDay8(unittest.TestCase):

	# Part 1 tests
	def test1(self):
		width = 3
		height = 2
		layers = breakIntoLayers('123456789012', width * height)
		self.assertEqual(layers[0], '123456')
		self.assertEqual(layers[1], '789012')

	# Part 2 tests
	def test2(self):
		width = 2
		height = 2
		layers = breakIntoLayers('0222112222120000', width * height)
		self.assertEqual(condenseLayers(layers), '0110')

if __name__ == '__main__':
	# unittest.main()
	# Part 1: 2318
	print(part1())
	# Part 2: AHFCB
	print(part2())
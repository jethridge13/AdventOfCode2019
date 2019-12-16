import unittest
from IntCode import IntCode

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def inputToArray(inp):
	return list(map(int, inp.split(',')))

def part1():
	data = load('Day5.txt')
	comp = IntCode.IntCode()
	data = IntCode.inputToArray(data)
	comp.start(data)

def part2():
	pass

class TestDay5(unittest.TestCase):

	def test1(self):
		pass

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 
	print(part1())
	# Part 2: 
	print(part2())
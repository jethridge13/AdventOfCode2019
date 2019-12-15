import unittest
import IntCode

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def part1():
	data = load('Day5.txt')
	data = IntCode.inputToArray(data)
	IntCode.start(data)

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
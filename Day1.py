import unittest

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def calcFuel(mass):
	return (mass // 3) - 2

def part1():
	data = load('Day1.txt')
	data = data.split()
	sum = 0
	for line in data:
		sum += calcFuel(int(line))
	return sum

class TestDay1(unittest.TestCase):

	def test1(self):
		mass = 12
		self.assertEqual(calcFuel(mass), 2)

	def test2(self):
		mass = 14
		self.assertEqual(calcFuel(mass), 2)

	def test3(self):
		mass = 1969
		self.assertEqual(calcFuel(mass), 654)

	def test4(self):
		mass = 100756
		self.assertEqual(calcFuel(mass), 33583)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 3560353
	print(part1())
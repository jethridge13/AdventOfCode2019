import unittest

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def calcFuel(mass):
	fuel = (mass // 3) - 2
	if fuel < 0:
		fuel = 0
	return fuel

def calcFuel2(mass):
	if mass == 0:
		return 0
	fuel = calcFuel(mass)
	return fuel + calcFuel2(fuel)

def part1():
	data = load('Day1.txt')
	data = data.split()
	sum = 0
	for line in data:
		sum += calcFuel(int(line))
	return sum

def part2():
	data = load('Day1.txt')
	data = data.split()
	sum = 0
	for line in data:
		sum += calcFuel2(int(line))
	return sum

class TestDay1(unittest.TestCase):

	# Part 1 Tests
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

	# Part 2 Tests
	def test5(self):
		mass = 14
		self.assertEqual(calcFuel2(mass), 2)

	def test6(self):
		mass = 1969
		self.assertEqual(calcFuel2(mass), 966)

	def test7(self):
		mass = 100756
		self.assertEqual(calcFuel2(mass), 50346)

if __name__ == '__main__':
	# unittest.main()
	# Part 1: 3560353
	print(part1())
	# Part 2: 5337642
	print(part2())
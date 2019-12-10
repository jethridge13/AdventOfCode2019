import unittest
import re

def breakIntoRanges(range):
	limits = range.split('-')
	limits[0] = int(limits[0])
	limits[1] = int(limits[1])
	return limits

def isValid(n, minVal=0, maxVal=1000000):
	repeatedChars = r'([0-9])\1'
	increasing = r'^(?=\d{6}$)0*1*2*3*4*5*6*7*8*9*$'
	match = re.search(increasing, n)
	if not match:
		return False
	match = re.search(repeatedChars, n)
	if not match:
		return False
	return True

def part1(limits):
	limits = breakIntoRanges(limits)
	count = 0
	for i in range(limits[0], limits[1]):
		if isValid(str(i)):
			count += 1
	return count

def part2():
	pass

class TestDay4(unittest.TestCase):

	def test1(self):
		inp = '1-5'
		outp = [1,5]
		self.assertEqual(breakIntoRanges(inp), outp)

	def test2(self):
		inp = '124075-580769'
		outp = [124075,580769]
		self.assertEqual(breakIntoRanges(inp), outp)

	def test4(self):
		self.assertFalse(isValid('1'))

	def test5(self):
		self.assertFalse(isValid('123456'))

	def test6(self):
		self.assertFalse(isValid('654321'))

	def test7(self):
		self.assertFalse(isValid('665432'))

	def test8(self):
		self.assertFalse(isValid('112315'))
	
	def test9(self):
		inp = '112345'
		self.assertTrue(isValid(inp))

if __name__ == '__main__':
	# unittest.main()
	inp = '124075-580769'
	# Part 1: 2150
	print(part1(inp))
	# Part 2:
	print(part2())
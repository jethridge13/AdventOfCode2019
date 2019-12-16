import unittest
from IntCode import IntCode
from IntCode import inputToArray

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

class IntCodeTest(unittest.TestCase):

	def testDay2Part1(self):
		inp = load('Day2.txt')
		data = inputToArray(inp)
		data[1] = 12
		data[2] = 2
		comp = IntCode()
		resp = comp.start(data)
		print(resp)
		self.assertEqual(resp[0], 3850704)

if __name__ == '__main__':
	unittest.main()
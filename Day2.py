import unittest

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.read()
	return data

def inputToArray(input):
	return list(map(int, input.split(',')))

def run(data):
	index = 0
	while data[index] != 99:
		# Get opcode and registers
		opcode = data[index]
		reg1Index = data[index+1]
		reg1 = data[reg1Index]
		reg2Index = data[index+2]
		reg2 = data[reg2Index]
		des = data[index+3]
		# Increment index counter
		index += 4
		# Perform operation
		if opcode == 1:
			result = reg1 + reg2
			data[des] = result
		elif opcode == 2:
			result = reg1 * reg2
			data[des] = result
		elif opcode == 99:
			break;
		else:
			raise Exception('An invalid opcode has been encountered: %s' % opcode)
	return data

def part1():
	data = load('Day2.txt')
	data = inputToArray(data)
	data[1] = 12
	data[2] = 2
	data = run(data)
	return data[0]

def part2():
	pass

class TestDay2(unittest.TestCase):

	# Part 1 Tests
	def test1(self):
		t = '1,2,3'
		self.assertEqual(inputToArray(t), [1, 2, 3])

	def test2(self):
		t = '1,9,10,3,2,3,11,0,99,30,40,50'
		self.assertEqual(inputToArray(t), [1,9,10,3,2,3,11,0,99,30,40,50])

	def test3(self):
		t = '1,0,0,0,99'
		t = inputToArray(t)
		self.assertEqual(run(t), [2,0,0,0,99])

	def test4(self):
		t = '2,3,0,3,99'
		t = inputToArray(t)
		self.assertEqual(run(t), [2,3,0,6,99])

	def test5(self):
		t = '2,4,4,5,99,0'
		t = inputToArray(t)
		self.assertEqual(run(t), [2,4,4,5,99,9801])

	def test6(self):
		t = '1,1,1,4,99,5,6,0,99'
		t = inputToArray(t)
		self.assertEqual(run(t), [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 3850704
	print(part1())
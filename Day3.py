import unittest

def load(path):
	pass

def parseInstruction(ins):
	direction = ins[0]
	length = int(ins[1:])
	return (direction, length)

class TestDay3(unittest.TestCase):

	def test1(self):
		self.assertEqual(parseInstruction('U13'), ('U', 13))

	def test2(self):
		self.assertEqual(parseInstruction('R9999'), ('R', 9999))
	
if __name__ == '__main__':
	unittest.main()

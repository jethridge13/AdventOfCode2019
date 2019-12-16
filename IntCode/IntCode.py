class IntCode():

	cursor = 0
	ins = []

	def incrementCursor(self, opcode):
		if opcode == 1 or opcode == 2:
			self.cursor += 4
		if opcode == 3 or opcode == 4:
			self.cursor += 2

	def getInstruction(self, inp):
		# TODO Add in mode parameters
		data = {}
		data['1'] = 0
		data['2'] = 0
		data['3'] = 0
		# TODO This special handling can be removed since the general case
		# should also cover it
		if len(str(inp)) == 1:
			data['opcode'] = inp
			data['3'] = 1
			data = self.getValues(data)
			return data
		# TODO Handling for bigger instructions
		return data

	def getValues(self, data):
		# TODO This could be accomplished with a loop in a different data shape
		if data['1'] == 0:
			register1 = self.ins[self.cursor+1]
			data['value1'] = self.ins[register1]
		else:
			data['value1'] = self.ins[self.cursor+1]
		if data['2'] == 0:
			register2 = self.ins[self.cursor+2]
			data['value2'] = self.ins[register2]
		else:
			data['value2'] = self.ins[self.cursor+2]
		if data['3'] == 0:
			register3 = self.ins[self.cursor+3]
			data['value3'] = self.ins[register3]
		else:
			data['value3'] = self.ins[self.cursor+3]
		return data

	'''
	Executes the given instruction
	Returns True if execution should continue
	Returns False if encountered the End opcode, signalling a halt
	'''
	def executeInstruction(self, instruction):
		# Day 2 opcodes
		opcode = instruction['opcode']
		if opcode == 1:
			# Add two values
			result = instruction['value1'] + instruction['value2']
			self.ins[instruction['value3']] = result
		elif opcode == 2:
			# Multiply two values
			result = instruction['value1'] * instruction['value2']
			self.ins[instruction['value3']] = result
		# Day 5 opcodes
		elif opcode == 3:
			# Ask for user input
			self.ins[reg1Index] = input()
		elif opcode == 4:
			# Print output
			print(reg1)
		elif opcode == 99:
			return False
		else:
			raise Exception('An invalid opcode has been encountered: %s' % opcode)
		return True
	
	def run(self):
		while self.ins[self.cursor] != 99:
			# Get opcode and registers
			instruction = self.getInstruction(self.ins[self.cursor])
			# Perform operation
			if not self.executeInstruction(instruction):
				return data
			# Increment cursor to move to next instruction
			self.incrementCursor(instruction['opcode'])
		return self.ins

	def start(self, data):
		self.ins = data
		return self.run()

# ------------------------------------------
# External Helper Functions
# ------------------------------------------
def inputToArray(inp):
	return list(map(int, inp.split(',')))
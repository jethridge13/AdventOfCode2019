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
		if len(inp) == 1:
			data['opcode'] = inp
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

	def executeInstruction(self, instruction):
		# Day 2 opcodes
		opcode = instruction['opcode']
		if opcode == 1:
			# Add two values
			result = reg1 + reg2
			data[des] = result
		elif opcode == 2:
			# Multiply two values
			result = reg1 * reg2
			data[des] = result
		# Day 5 opcodes
		elif opcode == 3:
			# Ask for user input
			data[reg1Index] = input()
		elif opcode == 4:
			# Print output
			print(reg1)
		elif opcode == 99:
			break;
		else:
			raise Exception('An invalid opcode has been encountered: %s' % opcode)
	
	def run(self):
		while self.ins[self.cursor] != 99:
			# Get opcode and registers
			instruction = self.getInstruction(self.ins[self.cursor])
			# TODO Update this for Day 5
			opcode = data[index]
			reg1Index = data[index+1]
			reg1 = data[reg1Index]
			reg2Index = data[index+2]
			reg2 = data[reg2Index]
			des = data[index+3]
			# Perform operation
			self.executeInstruction(instruction)
			# Increment cursor to move to next instruction
			self.incrementCursor(opcode)
		return data

	def start(self, data):
		self.ins = data
		self.run()
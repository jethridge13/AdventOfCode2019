class IntCode():

	def getOpcodeAndMode(inp):
		data = {}
		data['1'] = 0
		data['2'] = 0
		data['3'] = 0
		if len(inp) == 1:
			data['opcode'] = inp
			return data

	
	def run(self, data):
		index = 0
		while data[index] != 99:
			# Get opcode and registers
			# TODO Update this for Day 5
			opcode = data[index]
			reg1Index = data[index+1]
			reg1 = data[reg1Index]
			reg2Index = data[index+2]
			reg2 = data[reg2Index]
			des = data[index+3]
			# Increment index counter
			# TODO Change incrementer
			index += 4
			# Perform operation
			# Day 2 opcodes
			if opcode == 1:
				result = reg1 + reg2
				data[des] = result
			elif opcode == 2:
				result = reg1 * reg2
				data[des] = result
			elif opcode == 3:
				data[reg1Index] = input()
			elif opcode == 4:
				print(reg1)
			elif opcode == 99:
				break;
			else:
				raise Exception('An invalid opcode has been encountered: %s' % opcode)
		return data
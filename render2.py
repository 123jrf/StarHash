
MerlianParts = ['/\\\n/--\\\n|__|', '|::|', '\'\+/', '\+/\'', './:|',  '|:\\.', '/|=', '=|\\', ' ** ', ' || ', '||', '/\'\'\\' ]

ParasolParts = ['/', '\\']

# Takes a ship object and returns a rendered ship string
def drawShip(ship):
	shipString = ''
	
	shipSize = ship.blocks
	
	shipBlocks = [ship.weapons, ship.armor, ship.engines, ship.misc]
	
	shipBlockTotals = [sum(ship.weapons), sum(ship.armor), sum(ship.engines), sum(ship.misc)]
	
	if ship.brand == 1:
		# Parasol Corps.
		shipString = genParasolShape(shipSize, shipBlocks, shipBlockTotals)
	elif ship.brand == 2:
		# Melian Incorporated
		shipString =  genMelianShape(shipSize, shipBlocks, shipBlockTotals)
	elif ship.brand == 3:
		# Grah-Zin Star Cruisers
		shipString = genGrahzinShape(shipSize, shipBlocks, shipBlockTotals)
	elif ship.brand == 4:
		# Veias Intelligency
		shipString =   genVeiasShape(shipSize, shipBlocks, shipBlockTotals)
	
	return shipString


def genMelianShape(shipSize, shipBlocks, shipBlockTotals):
	
	shipShape = []
	
	tempSize = shipSize;
	
	if shipSize <= 4:
		for i in range(0,shipSize):
			shipShape.append(['#'])
			
	elif shipSize <= 10:	
		if shipSize%2 != 0:
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 3
		else:
			shipShape.append(['#'])
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 4
		
		for i in range(0,tempSize // 2):
			shipShape.append(['#','#'])
			tempSize -= 2
			
	elif shipSize <= 20:	
		if shipSize%2 != 0:
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 3
		else:
			shipShape.append(['#'])
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 4	
		
		for i in range(0,(tempSize-(4*(tempSize // 4))) // 2):
			shipShape.append(['#','#'])
			tempSize -= 2
		
		for i in range(0,tempSize // 4):
			shipShape.append(['#','#','#','#'])
			tempSize -= 4
	
	elif shipSize <= 36:	
		if shipSize%2 != 0:
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 3
		else:
			shipShape.append(['#'])
			shipShape.append(['#'])
			shipShape.append(['#','#'])
			tempSize -= 4	
		
		for i in range(0,((tempSize-(6*(tempSize/6)))-(4*((tempSize-(6*(tempSize/6)))/4)))/2):
			shipShape.append(['#','#'])
			tempSize -= 2
		
		for i in range(0,(tempSize-(6*(tempSize/6)))/4):
			shipShape.append(['#','#','#','#'])
			tempSize -= 4
			
		for i in range(0,tempSize/6):
			shipShape.append(['#','#','#','#','#','#'])
			tempSize -= 6
	
	return genMelianShip(shipShape, shipSize)

def genMelianShip(shipLayout, shipSize):
	
	shipString = ''
	
	if shipSize > 4:
		
		minlength = 2
		length = len(shipLayout)
		
		if shipSize%2 != 0:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[4]
			shipLayout[1][1] = MerlianParts[5]
		else:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[1]
			shipLayout[2][0] = MerlianParts[4]
			shipLayout[2][1] = MerlianParts[5]
			minlength = 3
		
		for i in range(minlength, length-2):
			if len(shipLayout[i]) == 2:
				shipLayout[i][0] = MerlianParts[1]
				shipLayout[i][1] = MerlianParts[1]
				
			if len(shipLayout[i]) == 4:
				shipLayout[i][0] = MerlianParts[9]
				shipLayout[i][1] = MerlianParts[1]
				shipLayout[i][2] = MerlianParts[1]
				shipLayout[i][3] = MerlianParts[9]
				
			if len(shipLayout[i]) == 6:
				shipLayout[i][0] = MerlianParts[10]
				shipLayout[i][1] = MerlianParts[9]
				shipLayout[i][2] = MerlianParts[1]
				shipLayout[i][3] = MerlianParts[1]
				shipLayout[i][4] = MerlianParts[9]
				shipLayout[i][5] = MerlianParts[10]
				
		if shipSize <= 10:
			shipLayout[length-2][0] = MerlianParts[1]
			shipLayout[length-2][1] = MerlianParts[1]
			shipLayout[length-1][0] = MerlianParts[2]
			shipLayout[length-1][1] = MerlianParts[3]
	
		if shipSize > 10 and shipSize <= 20:
			shipLayout[length-2][1] = MerlianParts[1]
			shipLayout[length-2][2] = MerlianParts[1]
			shipLayout[length-2][0] = MerlianParts[6]
			shipLayout[length-2][3] = MerlianParts[7]
			shipLayout[length-1][1] = MerlianParts[2]
			shipLayout[length-1][2] = MerlianParts[3]
			shipLayout[length-1][0] = MerlianParts[8]
			shipLayout[length-1][3] = MerlianParts[8]
		
		if shipSize > 20:
			shipLayout[length-2][2] = MerlianParts[1]
			shipLayout[length-2][3] = MerlianParts[1]
			shipLayout[length-2][1] = MerlianParts[6]
			shipLayout[length-2][4] = MerlianParts[7]
			shipLayout[length-2][0] = MerlianParts[6]
			shipLayout[length-2][5] = MerlianParts[7]
			
			shipLayout[length-1][2] = MerlianParts[2]
			shipLayout[length-1][3] = MerlianParts[3]
			shipLayout[length-1][1] = MerlianParts[8]
			shipLayout[length-1][4] = MerlianParts[8]
			shipLayout[length-1][0] = MerlianParts[8]
			shipLayout[length-1][5] = MerlianParts[8]
		
	else:
		if shipSize == 1:
			shipLayout[0][0] = MerlianParts[0]
		elif shipSize == 2:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[11]
		elif shipSize == 3:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[1]
			shipLayout[2][0] = MerlianParts[11]
		elif shipSize == 4:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[1]
			shipLayout[2][0] = MerlianParts[1]
			shipLayout[3][0] = MerlianParts[11]
		
		
	shipString = ''
	
	maxWidth = 0
	for i in range(0,len(shipLayout)):
		if len(shipLayout[i]) > maxWidth:
			maxWidth = len(shipLayout[i])
	maxWidth *= 4
	
	splits = shipLayout[0][0].split('\n')
	for i in splits:
		shipString += stringCenter(i, maxWidth) + '\n'
	
	for i in range(1,len(shipLayout)):
		section = ''
		for n in range(0,len(shipLayout[i])):
			section += shipLayout[i][n]
		shipString += stringCenter(section, maxWidth) + '\n'

	print(shipString)
	
	return shipString

def genParasolShape(shipSize, shipBlocks, shipBlockTotals):
	
	shipShape = []
	
	tempSize = shipSize;
	
	if shipSize <= 4:
		# Width 1
		for i in range(0,shipSize):
			shipShape.append(['#'])
			
	elif shipSize <= 11:
		# Width 2
		for i in range(0, shipSize // 2):
			shipShape.append(['#','#'])
			
		if shipSize%2 != 0:
			shipShape.append(['#'])
			
	elif shipSize <= 22:
		# Width 3
		for i in range(0,shipSize/3):
			shipShape.append(['#','#','#'])
			tempSize -= 3
		
		if tempSize == 2:
			shipShape.append(['#','#'])
		elif tempSize == 1:
			shipShape.append(['#'])
				
	elif shipSize <= 36:
		# Width 4
		for i in range(0,shipSize/4):
			shipShape.append(['#','#','#','#'])
			tempSize -= 4
		
		if tempSize == 3:
			shipShape.append(['#','#','#'])
		elif tempSize == 2:
			shipShape.append(['#','#'])
		elif tempSize == 1:
			shipShape.append(['#'])
	
	return genParasolShip(shipShape, shipSize)

def genParasolShip(shipLayout, shipSize):
	
	shipString = ''
	
	if shipSize > 4:
		
		minlength = 1
		length = len(shipLayout)
		width = len(shipLayout[0])
		print(len(shipLayout[0]))
		print(ParasolParts[0])
		
		shipLayout[0][0] = ParasolParts[0]
		shipLayout[0][width-1] = ParasolParts[1]
		
		'''for i in range(minlength, length-2):
			if len(shipLayout[i]) == 2:
				shipLayout[i][0] = MerlianParts[1]
				shipLayout[i][1] = MerlianParts[1]
				
			if len(shipLayout[i]) == 3:
				shipLayout[i][0] = MerlianParts[9]
				shipLayout[i][1] = MerlianParts[1]
				shipLayout[i][2] = MerlianParts[1]
				
			if len(shipLayout[i]) == 4:
				shipLayout[i][0] = MerlianParts[10]
				shipLayout[i][1] = MerlianParts[9]
				shipLayout[i][2] = MerlianParts[1]
				shipLayout[i][3] = MerlianParts[1]'''
			
			
		
	'''else:
		if shipSize == 1:
			shipLayout[0][0] = MerlianParts[0]
		elif shipSize == 2:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[11]
		elif shipSize == 3:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[1]
			shipLayout[2][0] = MerlianParts[11]
		elif shipSize == 4:
			shipLayout[0][0] = MerlianParts[0]
			shipLayout[1][0] = MerlianParts[1]
			shipLayout[2][0] = MerlianParts[1]
			shipLayout[3][0] = MerlianParts[11]'''
		
	
	maxWidth = 0
	for i in range(0,len(shipLayout)):
		if len(shipLayout[i]) > maxWidth:
			maxWidth = len(shipLayout[i])
	maxWidth *= 4
	
	for i in range(1,len(shipLayout)):
		section = ''
		for n in range(0,len(shipLayout[i])):
			section += shipLayout[i][n]
		shipString += stringCenter(section, maxWidth) + '\n'

	print(shipString)
	
	return shipString

def genBasicShip(shipLayout):
	
	shipString = ''
	
	maxWidth = 0
	for i in range(0,len(shipLayout)):
		if len(shipLayout[i]) > maxWidth:
			maxWidth = len(shipLayout[i])
	maxWidth *= 4
	
	for i in range(0,len(shipLayout)):
		section = ''
		for n in range(0,len(shipLayout[i])):
			section += shipLayout[i][n]
		shipString += stringCenter(section, maxWidth) + '\n'

	print(shipString)
	
	return shipString

def stringCenter(string, width):
	spacesNum = width - len(string)
	spaces = ''
	for i in range(0, spacesNum // 2):
		spaces += ' '
	string = spaces + string + spaces
	'''if spacesNum%2!=0:
		string = ' ' + string'''
	return string
	

if __name__ == "__main__":
	#genParasolShape(10, [[1,0,0],[3,2,1],[0,0,1],[2,1,2]], [1,6,1,5])
	genMelianShape(14, [[2,0,0],[6,4,2],[0,0,2],[4,2,4]], [2,12,2,10])
	#genMelianShape(36, [], [])

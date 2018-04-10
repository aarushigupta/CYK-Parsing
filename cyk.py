import itertools

def parseGrammar(production, grammarDict):
	arrowIndex = production.find('->') + 1
	leftSide = production[0:arrowIndex - 1]
	rightSide = production[arrowIndex + 1 :]
	while (len(rightSide)):
		prodSeparatorIndex = rightSide.find('|')
		if prodSeparatorIndex == -1:
			if rightSide in grammarDict.keys():
				grammarDict[rightSide].append(leftSide)
			else:
				grammarDict[rightSide] = [leftSide]
			break
		else:
			prod = rightSide[0:prodSeparatorIndex]
			if prod in grammarDict.keys():
				grammarDict[prod].append(leftSide)
			else:
				grammarDict[prod] = [leftSide]
			rightSide = rightSide[prodSeparatorIndex+1 :]
	return grammarDict

def checkLeftSide(production):
	arrowIndex = production.find('->')
	leftSide = production[0:arrowIndex]
	if len(leftSide) == 1 and leftSide[0] >= 'A' and leftSide[0] <='Z':
		return 1
	else:
		return 0

def checkRightSide(production):
	arrowIndex = production.find('->')
	rightSide = production[arrowIndex + 2:]

	while (len(rightSide)):
		prodSeparatorIndex = rightSide.find('|')
		if prodSeparatorIndex == -1:
			if len(rightSide) == 2 and rightSide[0] >= 'A' and rightSide[0] <= 'Z' and rightSide[1] >= 'A' and rightSide[1] <= 'Z':
				return 1
		else:
			prod = rightSide[0:prodSeparatorIndex]
			if len(prod) == 2 and prod[0] >= 'A' and prod[0] <= 'Z' and prod[1] >= 'A' and prod[1] <= 'Z':
				return 1
			rightSide = rightSide[prodSeparatorIndex+1 :]

	return 0


def makeTableforString(string, grammarDict):
	decisionTable = [[[] for x in range(len(string))] for y in range(len(string))]
	for i in range(len(string) - 1, -1, -1):
		if i == len(string) - 1 :
			for j in range(len(string)):
				if string[j] in grammarDict.keys():
					decisionTable[i][j] = grammarDict[string[j]]
				else:
					decisionTable[i][j] = []

		else:
			for j in range(i + 1):
				verticalRow = len(string) - 1
				verticalCol = j
				diagonalRow = i + 1
				diagonalCol = j + 1
				product = []
				while verticalRow > i:
					print verticalRow, verticalCol, diagonalRow, diagonalCol
					product += crossproduct(decisionTable[verticalRow][verticalCol], decisionTable[diagonalRow][diagonalCol])
					verticalRow -= 1
					diagonalRow += 1
					diagonalCol += 1
				result = giveFinalList(product, grammarDict)
				print "RRRRRRRRR : ", result
				decisionTable[i][j] = result

	print decisionTable



def giveFinalList(product, grammarDict):
	product = list(set(product))
	result = []
	for item in product:
		if item in grammarDict.keys():
			print "HELLLLLLLLO : ", grammarDict[item]
			result +=grammarDict[item]
	print "Result in FinalList: ", result

	result = list(set(result))

	return result

def crossproduct(item1, item2):
	print "Item1: ", item1
	print "Item2: ", item2
	result = list(itertools.product(item1, item2))
	print "Result: ", result
	resultStr = []
	for item in (itertools.product(item1, item2)):
		resultStr.append(''.join(item))

	print "Result appended: ", resultStr

	return resultStr


if __name__ == '__main__':
	grammarDict = {}
	#n = int(raw_input("Enter the no. of rules: "))
	n = 4

	arr = ['S->AB|BC', 'A->BA|a', 'B->CC|b', 'C->AB|a']

	for i in range(len(arr)):
		prodRule = arr[i]
		grammarDict = parseGrammar(prodRule, grammarDict)
	# for i in range(n):
	# 	prodRule = raw_input("Enter a rule: ")
	# 	grammarDict = parseGrammar(prodRule, grammarDict)

	string = raw_input("Enter the string whose membership is to be determined: ")

	print grammarDict

	makeTableforString(string, grammarDict)

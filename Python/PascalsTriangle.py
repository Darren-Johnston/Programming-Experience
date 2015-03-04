# Used for printing to the screen purposes
def printList(list):
	for i in list:
		print i
		
# Used to add the entire triangle to one string
def addTotalString(row, string):
	for i in row:
		string += str(i) + "  "
	return string

# Calculates the next number in the row	
def calculateNumber(count, prevRow):
	number = prevRow[count-1] + prevRow[count]
	return number
	
# Fill the previous row cleanly	
def fillPreviousRow (currRow):
	count = 0
	prevRow = []
	for i in currRow:
		prevRow.append(currRow[count])
		count += 1
	
	return prevRow

# Logic used to calculate the row next in the sequence
def getNextRow(prevRow):
	length = len(prevRow)
	newLength = length + 1 # Length of next row
	currRow = []
	for i in range (newLength):
		if (i == 0):
			currRow.append(1) # First number in row
		
		elif (i == newLength -1):
			currRow.append(1) # Last number in row
			
		else:
			currRow.append(calculateNumber(i, prevRow)) # Middle numbers in row
	
	
	return currRow

#Main Area of the Program#

done = False
decision = ""
while (done == False):
	firstNum = 1 # Used to input the first row
	currentRow = [firstNum] # The row that is being calculated from the previous row
	previousRow = [] # Used to calculate the next row
	count = 1 # Starting number for outputing rows
	totalString = "" # Used to output the entire triangle
	input = 0 # User number

	while (input <= 0):
		input = int(raw_input("Please enter number of rows: "))

	totalString += str(firstNum) + "\n" 
		
		
	while (count < input):
		previousRow = fillPreviousRow(currentRow)
		currentRow = getNextRow(previousRow)
		totalString = addTotalString(currentRow, totalString)
		totalString += "\n"
		count += 1
		

	print(totalString) # Prints entire triangle
	print("\n")
	decision = raw_input("Type yes to continue or no to quit: ")
	decision = decision.lower()
	if (decision == "no" or decision == "n"):
		done = True 
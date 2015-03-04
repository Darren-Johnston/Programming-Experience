# y = mx+b, slope = m 
#(3,2), (5,3)

import math
#print(dir(math))
#math.fabs

orderedSet = raw_input("Please enter the first ordered pair separated with a Comma: ")
otherSet = raw_input("Please enter the second ordered pair separated with a Comma: ")

orderedReplaced = orderedSet.replace(",", " ")
orderedReplaced = orderedReplaced.split()
otherReplaced  = otherSet.replace(",", " ")
otherReplaced = otherReplaced.split()

#print(orderedReplaced)
#print(otherReplaced)


orderedIntList = []
otherIntList = []
integer = 0
count = 0
for item in orderedReplaced:
	integer = int(item)
	orderedIntList.append(integer)
	
for string in otherReplaced:
	integer = int(string)
	otherIntList.append(integer)
	

slopeNum = (otherIntList[1] - orderedIntList[1])
slopeDenom = (otherIntList[0] - orderedIntList[0])

print("\n")
print("The original slope is: " + str(slopeNum) + "/" + str(slopeDenom))
exitStrategy = 1

if slopeDenom != 0:

	while slopeNum % 2 == 0 and slopeDenom %2 == 0 or slopeNum % 3 == 0 and slopeDenom % 3 == 0 or slopeNum % 5 == 0 and slopeDenom % 5 == 0 or slopeNum % 7 == 0 and slopeDenom % 7 == 0 or slopeNum % 11 == 0 and slopeDenom % 11 == 0 and exitStrategy != 0:
	#while slopeDenom % 2 == 0 or slopeDenom % 3 == 0 or slopeDenom % 5 == 0 or slopeDenom % 7 == 0 or slopeDenom % 11 == 0:
	#while slopeDenom % 2 == 0 or slopeDenom % 3 == 0 or slopeDenom % 5 == 0 or slopeDenom % 7 == 0 or slopeDenom % 11 == 0:

		if slopeNum % 2 == 0 and slopeDenom % 2 == 0:
			slopeNum = slopeNum / 2
			slopeDenom = slopeDenom / 2
			#print(fractionSimplify)
		elif slopeNum % 3 == 0 and slopeDenom % 3 == 0:
			slopeNum = slopeNum / 3
			slopeDenom = slopeDenom / 3
			#print(fractionSimplify)

		elif slopeNum % 5 == 0 and slopeDenom % 5 == 0:
			slopeNum = slopeNum / 5
			slopeDenom = slopeDenom / 5
			#print(fractionSimplify)

		elif slopeNum % 7 == 0 and slopeDenom % 7 == 0:
			slopeNum = slopeNum / 7
			slopeDenom = slopeDenom / 7
			#print(fractionSimplify)

		elif slopeNum % 11 == 0 and slopeDenom % 11 == 0:
			slopeNum = slopeNum / 11
			slopeNum = slopeDenom / 11
			#print(fractionSimplify)
		else:
			exitStrategy = 0
		#else:
			exitStrategy = 0


slopeNum = str(slopeNum)
slopeDenom = str(slopeDenom)

if "-" in slopeNum and "-" in slopeDenom:
	slopeNum = slopeNum.replace("-","")
	slopeDenom = slopeDenom.replace("-","")
	#print(slopeNum)
	#print(slopeDenom)
slopeNum = int(slopeNum)
slopeDenom = int(slopeDenom)

totalSlope = 0
if slopeDenom != 0:

	if slopeNum % slopeDenom == 0:
		if slopeNum == slopeDenom:
			totalSlope = str(1)
		elif math.fabs(slopeNum) == math.fabs(slopeDenom):
			totalSlope = str(-1)
		else:
			totalSlope = str(slopeNum) + "/" + str(slopeDenom)
	else:
		totalSlope = str(slopeNum) + "/" + str(slopeDenom)
else:
	totalSlope = "undefined"

totalSlope = str(totalSlope)
print("The simplified slope of this ordered pair is: " + totalSlope)

x = str(orderedIntList[0])
y = str(orderedIntList[1])

pointSlopeFormula = "y - " + y + " = " + totalSlope + "(x - " + x + ")"
print("The point slope for these ordered pairs is " + pointSlopeFormula)
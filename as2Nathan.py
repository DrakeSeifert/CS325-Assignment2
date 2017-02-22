import numpy
import pprint

cost = []
with open('imp2cost.txt') as inputfile:
	for line in inputfile:
		cost.append(line.strip().split(','))
inputfile.close()

inputChars = []
with open('imp2input.txt') as inputfile:
	for line in inputfile:
		inputChars.append(line.strip().split(','))
inputfile.close()
# print inputChars

pairVals = {}
for i in range(1, len(cost[0])): #col
	for j in range(1, len(cost[0])): #row
		pairVals[(cost[0][i], cost[j][0])] = cost[i][j]

stringTemp1 = []
stringTemp2 = []
for i in range(0, len(inputChars)):
	stringTemp1.append(inputChars[i][0])
	stringTemp2.append(inputChars[i][1])

i = 0
string1 = []
while i < len(stringTemp1):
	string1.append(list(stringTemp1[i]))
	i+=1

i = 0
string2 = []
while i < len(stringTemp2):
	string2.append(list(stringTemp2[i]))
	i+=1

def algorithm(string1, string2, pairVals):
        # * S T R 2
        # S
        # T
        # R
        # 1
        # For ptr, just ints so 1 is down, 2 is diagonal, 3 is left
        ptr = numpy.zeros((len(string1)+1,len(string2)+1), dtype=int)
        editCost = numpy.zeros((len(string1)+1, len(string2)+1), dtype=int)
	#Base case
        editCost[0][0] = 0
        for i in range(len(string1)):
                editCost[i+1][0] = editCost[i-1][0] + int(pairVals[(string1[i], '-')])
                ptr[i+1][0] = 1  #Down for delete
        for i in range(len(string2)):
                editCost[0][i+1] = editCost[0][i+1] + int(pairVals[(string2[i], '-')])
                ptr[0][i+1] = 3  #Left for insert

        for i in range(1, len(string1)):
                for j in range(1, len(string2)):
                        alignCost = editCost[i-1][j-1] + int(pairVals[(string1[i-1], string2[j-1])])
                        insertCost = editCost[i][j-1] + int(pairVals[('-',string2[j-1])])
                        deleteCost = editCost[i-1][j] + int(pairVals[(string1[i-1],'-')])
                        if(alignCost <= insertCost and alignCost <= deleteCost):
                                #Align
                                editCost[i][j] = alignCost
                                ptr[i][j] = 2#Diagonal
                        elif(insertCost <= alignCost and insertCost <= deleteCost):
                                #Insert
                                editCost[i][j] = insertCost
                                ptr[i][j] = 3#Left
                        elif(deleteCost <= insertCost and deleteCost <= alignCost):
                                #Delete
                                editCost[i][j] = 1#Down
                        else:
                                print "Somethings strange in the neighborhoodz"
	#return the minimum of the 3 cases
        print editCost
# answers = []
# for i in range(0, len(inputChars)):
# 	answers.append(algorithm(string1[i], string2[i], pairVals))

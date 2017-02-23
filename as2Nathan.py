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

pairVals = {}
for i in range(1, len(cost[0])): #col
	for j in range(1, len(cost[0])): #row
		pairVals[(cost[0][i], cost[j][0])] = cost[i][j]

string1 = []
string2 = []
for i in range(0, len(inputChars)):
	string1.append(inputChars[i][0])
	string2.append(inputChars[i][1])

def algorithm(string1, string2, pairVals):
        # * S T R 2
        # S
        # T
        # R
        # 1
        # For ptr, just ints so 1 is down, 2 is diagonal, 3 is left
        width = len(string2)+1
        height = len(string1)+1
        ptr = [[-1]*width for x in range(height)]
        editCost = [[-1]*width for x in range(height)]

        c1 = c2 = ''
        out1 = out2 = ""
        direct = 0
        
	#Base case
        editCost[0][0] = ptr[0][0] = 0
        for i in range(1, height):
                editCost[i][0] = editCost[i-1][0] + int(pairVals[(string1[i-1], '-')])
                ptr[i][0] = 1  #Down for delete
        for i in range(1, width):
                editCost[0][i] = editCost[0][i-1] + int(pairVals[(string2[i-1], '-')])
                ptr[0][i] = 3  #Left for insert

        for i in range(1, height):
                for j in range(1, width):
                        alignCost = editCost[i-1][j-1] + int(pairVals[(string1[i-1], string2[j-1])])
                        insertCost = editCost[i][j-1] + int(pairVals[('-',string2[j-1])])
                        deleteCost = editCost[i-1][j] + int(pairVals[(string1[i-1],'-')])
                        if(alignCost <= insertCost and alignCost <= deleteCost):
                                #Align
                                editCost[i][j] = alignCost
                                ptr[i][j] = 2 #Diagonal
                        elif(insertCost <= alignCost and insertCost <= deleteCost):
                                #Insert
                                editCost[i][j] = insertCost
                                ptr[i][j] = 3 #Left
                        elif(deleteCost <= insertCost and deleteCost <= alignCost):
                                #Delete
                                editCost[i][j] = deleteCost
                                ptr[i][j] = 1 #Down
                        else:
                                print "Somethings strange in the neighborhoodz"
        #Bactrace function
        #Start at bottom left value
        #Build strings from end
        i, j = height-1, width-1
        s1Idx, s2Idx = len(string1) - 1, len(string2)-1
        # print ptr[i][j]
        while i >=0 and j >= 0:
                direct = ptr[i][j]
                # print direct
                if direct == 1:
                        #Down or delete
                        out1 = string1[s1Idx] + out1
                        out2 = '-' + out2
                        s1Idx = s1Idx - 1
                        i = i-1
                elif direct == 2:
                        #Diagonal or align
                        out1 = string1[s1Idx] + out1
                        out2 = string2[s2Idx] + out2
                        s1Idx = s1Idx - 1
                        s2Idx = s2Idx - 1
                        i = i - 1
                        j = j - 1
                elif direct == 3:
                        #Left or insert
                        out1 = '-' + out1
                        out2 = string2[s2Idx] + out2
                        s2Idx = s2Idx - 1
                        j = j - 1
                elif ptr[i][j] == 0:
                        break
                else:
                        print "Invisible man sleeping in your bed"
                        exit(2)

        return out1, out2, editCost[height-1][width-1]

outFile = open("imp2output.txt", "w") #clear contents
outFile.close()
outFile = open("imp2output.txt", "a")
for i in range(0, len(inputChars)):
        out1, out2, cost = algorithm(string1[i], string2[i], pairVals)

        outFile.write(out1)
        outFile.write(",")
        outFile.write(out2)
        outFile.write(":")
        outFile.write(str(cost))
        outFile.write("\n")
outFile.close()
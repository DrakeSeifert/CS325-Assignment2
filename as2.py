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

#print pairVals

#example to access 1 inputChar chunk
# for i in range(0, len(inputChars[0][0])):
# 	print inputChars[0][0][i]

# print cost
# print "\n\n\n"
# print inputChars

#def algorithm(pairVals, inputChars):

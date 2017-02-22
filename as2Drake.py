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
#print pairVals

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

# print "temp1:\n", stringTemp1
# print "\n\n\n"
# print "string1:\n", string1
# print "\n\n\n"

i = 0
string2 = []
while i < len(stringTemp2):
	string2.append(list(stringTemp2[i]))
	i+=1

# print "temp2:\n", stringTemp2
# print "\n\n\n"
# print "string2:\n", string2
# print "\n\n\n"

#compare string1[0] with string2[0]
#        string1[1] with string2[1], etc.
def algorithm(string1, string2, pairVals):
	#Base case
	if(len(string1) == 1 or len(string2) == 1):
		return 999 #dummy value for now

	#return the minimum of the 3 cases

# answers = []
# for i in range(0, len(inputChars)):
# 	answers.append(algorithm(string1[i], string2[i], pairVals))

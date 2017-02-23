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

def alg(string1, string2):

	print "*************************************************"
	print string1
	print "\n"
	print string2
	print "*************************************************"

	#Calculate edit distance table
	EDT = [[-1 for x in range(len(string2)+1)] for y in range(len(string1)+1)]
	#T[0][0] starts at top left
	#string1 on y axis, string2 on x axis
	#Usage: T[string1][string2] or T[y-axis][x-axis]

	for i in range(0, len(EDT[0])):
		EDT[0][i] = i;

	for i in range(0, len(EDT)):
		EDT[i][0] = i

	for i in range(1, len(string1)+1):
		for j in range(1, len(string2)+1):
			if(string1[i-1] == string2[j-1]):
				EDT[i][j] = EDT[i-1][j-1]
			else:
				EDT[i][j] = 1 + min(EDT[i-1][j-1], EDT[i-1][j], EDT[i][j-1])

	for i in range(0, len(EDT)):
		print EDT[i]

	i = len(EDT) - 1
	j = len(EDT[0]) - 1

	# newString1 = string1
	# newString2 = string2

	#Find deletions, and substitutions
	while(True):

		if(i <= 0 or j <= 0):
			break

		if(string1[i - 1] == string2[j - 1]):
			i -= 1
			j -= 1
		elif(EDT[i][j] == EDT[i-1][j-1] + 1):
			print "Edit", string2[j-1],"at", j,"in string2 to",string1[i-1],"at",i,"in string1"
			i -= 1
			j -= 1
		elif(EDT[i][j] == EDT[i-1][j] + 1):
			print "Delete in string1: ", string1[i],"at",i
			i -= 1
		elif(EDT[i][j] == EDT[i][j-1] + 1):
			print "Delete in string2: ", string2[j-1],"at",j
			j -= 1
		else:
			print "Error"
			exit(1)

	print abs(i - j)
	return EDT[len(string1)][len(string2)]


print alg(string1[1], string2[1])
# print alg("exponential", "polynomial")

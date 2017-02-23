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

i = 0
string2 = []
while i < len(stringTemp2):
	string2.append(list(stringTemp2[i]))
	i+=1

# T = [[-1 for x in range(len(string2[0])+1)] for y in range(len(string1[0])+1)]

# for i in range(0, len(T[0])):
# 	T[0][i] = i;

# for i in range(0, len(T)):
# 	T[i][0] = i

# for i in range(1, len(string1[0])):
# 	for j in range(1, len(string2[0])):
# 		if(string1[0][i-1] == string2[0][j-1]):
# 			T[i][j] = T[i-1][j-1]
# 		else:
# 			T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])

# for i in range(0, len(T)):
# 	print T[i]

def alg(string1, string2, index):

	print len(string1)
	print len(string2)
	T = [[-1 for x in range(len(string2)+1)] for y in range(len(string1)+1)]
	#string1 on y axis, string2 on x axis

	for i in range(0, len(T[0])):
		T[0][i] = i;

	for i in range(0, len(T)):
		T[i][0] = i

	for i in range(1, len(string1)+1):
		for j in range(1, len(string2)+1):
			if(string1[i-1] == string2[j-1]):
				T[i][j] = T[i-1][j-1]
			else:
				T[i][j] = 1 + min(T[i-1][j-1], T[i-1][j], T[i][j-1])

	for i in range(0, len(T)):
		print T[i]

	#exit(0)

	i = len(T) - 1
	j = len(T[0]) - 1

	while(True):

		if(i <= 0 or j <= 0):
			break

		if(string1[i - 1] == string2[j - 1]):
			i -= 1
			j -= 1
		elif(T[i][j] == T[i-1][j-1] + 1):
			print "Edit", string2[j-1],"to",string1[i-1],"in string1"
			i -= 1
			j -= 1
		elif(T[i][j] == T[i-1][j] + 1):
			print "Delete in string1: ", string1[i-1]
			i -= 1
		elif(T[i][j] == T[i][j-1] + 1):
			print "Delete in string2: ", string2[j-1]
			j -= 1
		else:
			print "Error" #Infinite loop :(


print alg(string1[0], string2[0], 0)

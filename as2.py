

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

#omit the "*" character
myChars = [];
for i in range(1, len(cost[0])):
	myChars.append(cost[0][i])

#example to access 1 inputChar chunk
# for i in range(0, len(inputChars[0][0])):
# 	print inputChars[0][0][i]

print cost
print "\n\n\n"
print myChars
print "\n\n\n"
print inputChars
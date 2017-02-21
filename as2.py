

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

print len(cost[0])

#omit the "*" character
myChars = [];
for i in range(1, len(cost[0])):
	myChars.append(cost[0][i])

print cost
print "\n\n\n"
print myChars
print "\n\n\n"
print inputChars
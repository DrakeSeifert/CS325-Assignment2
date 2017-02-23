import sys
import random
import time

if (len(sys.argv) != 4):
    print "USAGE: python generator.py fileName.input numChars numSets"
    print "---Will only generate ATGC"
    exit();

pfile = open(str(sys.argv[1]), "w")

string1 = ""
string2 = ""
chars = ['A','T','C','G']
random.seed(time.time())
numChars = int(sys.argv[2])
numSets = int(sys.argv[3])
for i in range(numSets+1):
    for j in range(numChars+1):
        p = random.choice(chars)
        string1 = string1 + p
    for j in range(numChars - random.randint(0, numChars/2)):
        p = random.choice(chars)
        string2 = string2 + p
    pfile.write(string1)
    pfile.write(",")
    pfile.write(string2)
    pfile.write("\n")
    

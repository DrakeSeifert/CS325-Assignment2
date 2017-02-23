import random
import time

def gen(fileName, numChars, numSets):
    pfile = open(str(fileName), "w")

    string1 = ""
    string2 = ""
    chars = ['A','T','C','G']
    random.seed(time.time())
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
        

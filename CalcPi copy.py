import random
import pil
calcpi = 0
numflips= 0
total = 0

def coinflip():
    numheads = 0
    numtails = 0
    while numtails >= numheads:
        coin = random.randint(0,1)
        if coin == 0:
            numheads += 1
        else:
            numtails += 1
    return numheads/(numheads + numtails)

for i in range (0,100000000000000000000000000000000000000000):
    total += coinflip()
    numflips += 1
    calcpi = (total/numflips)*4
    print(calcpi)

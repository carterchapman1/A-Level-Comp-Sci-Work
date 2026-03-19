import random
import math
calcpi = 0
injustcircle = 0
inboth = 0
for i in range (0,1000000):
    randomnumberx = random.random()
    randomnumbery = random.random()
    if math.sqrt((randomnumberx*randomnumberx + randomnumbery*randomnumbery)) <= 1:
        injustcircle += 1
        inboth +=1
    else:
        inboth += 1
calcpi = ((injustcircle) / inboth)*4
print(calcpi)

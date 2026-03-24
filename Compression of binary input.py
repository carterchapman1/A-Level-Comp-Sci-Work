data = input("enter data like ABBABBBAAA\n")
dictionary = {"": 0}
output = []
current = ""
for char in data:
    combined = current + char
    if combined in dictionary:
        current = combined
    else:
        index = dictionary[current]
        output.append((index, char))
        dictionary[combined] = len(dictionary)
        current = ""
print(output)

outputstring = ""
i = 0
finished = False
while finished != True:
    outputlast = outputstring
    try:
        if output[i][0] == 0:
            outputstring += output[i][1]
    except IndexError:
        pass
    else:
        y = i
        curatedstring = ""
        complete = False
        while complete == False:
            if output[y][0] != 0:
                curatedstring = output[y][1] + curatedstring
                y = output[y][0]-1
            else:
                complete = True
        outputstring = outputstring + output[y][1] + curatedstring
    print(outputstring)
    if outputlast == outputstring:
        finished = True
    try:
        i+=1
        if output[i][0] == 0:
            print('problem')
    except IndexError:
        pass

print(outputstring)

userinputstring = str(input("Input a string!"))
lengthofstring = len(userinputstring)
userinputstring = userinputstring.lower()
listofvowels = ["a","e","i","o","u"]
vowellocations = []
vowels = []
for i in range(lengthofstring):
    for vowelindex in range(5):
        if userinputstring[i] == listofvowels[vowelindex]:
            vowels.append(listofvowels[vowelindex])
            vowellocations.append(i)

vowellocationlength = len(vowellocations)
vowelslength = len(vowels)
scrambledword = ""
countofvowels = 0
vowelsinverted = []
for x in range(0,vowelslength):
    vowelsinverted.append(vowels[vowelslength-x-1])
    



for k in range(lengthofstring):
    try:
        if k == vowellocations[countofvowels]:
            scrambledword = scrambledword + vowelsinverted[countofvowels]
            countofvowels +=1
        else:
            scrambledword = scrambledword + userinputstring[k]
    except IndexError:
        lengthremaining = lengthofstring - len(scrambledword)
        for i in range(0,lengthremaining):
            scrambledword = scrambledword + userinputstring[len(scrambledword)+i]


print(scrambledword)
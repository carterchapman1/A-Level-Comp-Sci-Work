import math
def dentobin(input):
    input = input.split(".")
    inputleft = int(input[0])
    try:   
        inputright = "0."
        inputright = float(inputright.join(input[1]))
    except ValueError:
        inputright = float(input[1])
    list1 = [0,0,0,0,0,0,0,0]
    list2 = [0,0,0,0,0,0,0,0]
    if inputleft != 0:
        for i in range (0, int(math.log(inputleft,2) + 1)):
            if inputleft/2 == inputleft//2:
                list1[len(list1) - i - 1] = 0
            else: 
                list1[len(list1) - i - 1] = 1
            inputleft = inputleft//2
    if round(inputright,3) != 0:
        i = 0
        while inputright.is_integer() != True:
            if inputright*2 >= 1:
                list2[i] = 1
                if inputright == 0.5:
                    inputright = inputright * 2
                else:
                    inputright = inputright % 1
                print(1)
            elif inputright*2 < 1: 
                list2[i] = 0
                inputright = inputright * 2
                print(2)
            i += 1
            print(inputright)
    print(list1, list2)



def dentohex(input):
    list1 = [0,0,0,0]
    list2 = [0,0,0,0]
    for i in range (0, int(math.log(input,2) + 1)):
        digit1 = input//16
        digit2 = input%16
        digits = [digit1,digit2]
        alphabet = ["A","B","C","D","E","F"]
        combined = ["",""]
        for i in range(0,2):
            if digits[i] == 0:
                combined[i] = str(digits[i])
            elif digits[i] < 10:
                combined.join(str(digits[i]))
            else:
                combined[i] = str((alphabet[digits[i]]))
    print(combined)
    print(digits)
            
            
def dentofracbin(input:str):
    input = input.split(".")
    list = [0,0,0,0,0,0,0,0]
    for i in range (0, int(math.log(input,2) + 1)):
        if input/2 == input//2:
            list[len(list) - i - 1] = 0
        else: 
            list[len(list) - i - 1] = 1
        input = input//2
        print(list)



input = str(input('Input a Denary number to turn into a bin \n'))
dentobin(input)


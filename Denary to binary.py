import math
def dentobin(input):
    list = [0,0,0,0,0,0,0,0]
    for i in range (0, int(math.log(input,2) + 1)):
        if input/2 == input//2:
            list[len(list) - i - 1] = 0
        else: 
            list[len(list) - i - 1] = 1
        input = input//2
        print(list)

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
            
            
                


input = int(input('Input a Denary number to turn into a hex \n'))
dentohex(input)


def DenaryToBinary(Input):
    BinaryList = [0,0,0,0,0,0,0,0]
    BinaryString = ""
    for i in range(0,8):
        dividedinput = Input % 2
        BinaryList[i] = dividedinput 
        Input = Input // 2
        BinaryString = (str(dividedinput) + BinaryString)
    print(f"The Reverse Binary of that Denary is {BinaryList}")
    print(f"The Binary of that Denary is {BinaryString}")


DigitInput = int(input("Please enter a digit to be converted!\n"))
DenaryToBinary(DigitInput)

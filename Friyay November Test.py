"""userinteger = int(input("enter a interger greater than 1 "))
product = 1
factor = 0
while product < userinteger:
    factor += 1
    product = product * factor

if userinteger == product:
    product = 1
    for n in range (1,(factor)):
        product = product * n
        print(n)
else:
    print("no result")"""



userword1 = input("please enter a word \n")
userword2 = input("please enter another word \n")
userword1 = userword1.lower()
userword2 = userword2.lower()
letters = []
correct = [-1] * len(userword1)
for i in range (0,len(userword2)):
    letters.append(userword2[i])
for i in range (0,len(userword1)):
    for y in range (0,len(letters)):
        if letters[y] == userword1[i]:
            correct[i] = 1

index = 0
for i in range (0,len(correct)):
    if correct[i] == 1:
        index += 1
if index == len(correct):
    print("Word 1 can be made by word 2")
else:
    print("Word 1 cannot be made by word 2")



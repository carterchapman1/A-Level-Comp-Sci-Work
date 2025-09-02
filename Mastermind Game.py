import random

correct = 0 
complete = 0
pos = ''
number = ''
numberlist = []
for i in range (4):
    randomnumber = str(random.randint(1,9))
    number = number + '' + randomnumber 
    numberlist.append(randomnumber)

print(number)
modechoice = input('Do you want Easy mode (0) or hard mode(1)\n')
while complete == 0:
    userguess = str(input('Guess a Number between 1 and 9\n'))
    for i in range(4):
        if userguess == numberlist[i]:
            correct = correct + 1
            if modechoice == '0':
                pos = pos + str((i+1)) + ', '
    if modechoice == '0':
        print(f'you have gotten {correct} numbers right, these are in positions {pos}!')
    else:
        print(f'you have gotten {correct} numbers right!')
    guessing = str(input('Do you want to guess the number?\n'))
    if guessing == 'Yes' or guessing == 'yes'  :
        numberguess = str(input('Guess the Number\n'))
        if numberguess ==number:
            complete = 1
        else: 
            print('Wrong')
            correct = 0
            pos = ''
    else: 
        correct = 0
        pos = ''
print('Well done you beat it')

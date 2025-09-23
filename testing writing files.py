def reading(file):
    filename = file
    with open(filename, 'r') as file:
        line = file.read()
        print(line)

def writing(file):
    finished = '0'
    filename = file
    with open(filename, 'w') as file:
        while finished == '0':
            amount = input('How many lines do you plan on entering\n')
            for i in range(int(amount)):
                line = input('Please enter some text line by line\n')
                file.write((line+'\n'))
            done = (input('Are you done\n'))
            if done == 'Yes':
                finished = '1'
    reading(filename)

def rewrite(file):
    finished = '0'
    filename = file
    linenumber = int(input('Enter the line number you want to rewrite\n'))
    with open(filename, 'r') as file:
        lines = file.readlines()
    text = input('Enter the text you want to rewrite\n') 
    lines[linenumber] = text + '\n'
    with open(filename, 'w') as file:
        file.writelines(lines)

    
menu = input('Do you want to read a file (1) or write a file (2) or rewrite lines in a file (3)\n')
file = input('Please enter the file name\n')
if menu == '1':
    reading(file)
elif menu == '2':
    writing(file)
elif menu == '3':
    rewrite(file)
else:
    print('Please input a valid input\n')


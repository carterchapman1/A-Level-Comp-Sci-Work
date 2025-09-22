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
            line = input('Please enter some text line by line\n')
            file.write((line+'\n'))
            done = (input('Are you done\n'))
            if done == 'Yes':
                finished = '1'
    reading(filename)

menu = input('Do you want to read a file (1) or write a file (2)\n')
file = input('Please enter the file name\n')
if menu == '1':
    reading(file)
elif menu == '2':
    writing(file)
else:
    print('Please input a valid input\n')


def reading(file):
    filename = file
    with open(filename, 'r') as file:
        line = file.read()
        print(line)

def writing(file):
    finished = False
    filename = file
    with open(filename, 'r') as file:
        while finished == False:
            line = input('Please enter some text line by line')
            file.write(line)

de



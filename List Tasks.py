name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
number_list = []
numbertotal = 0
for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)

print(name_list)
print('The third name is: ' + name_list[3])
print(f"The last 7 names are: {name_list[10:]}")
for i in range(5):
    number = int(input('Input a number\n'))
    numbertotal = numbertotal + number
    number_list.append(number)
number_list.sort(reverse= True)
print(number_list[0])
print(number_list[4])
print(numbertotal / 5)

    
tasks = []
done = 0
listindex = 0
while done == 0:
    option = input('Do you want to \n 1. Add a task \n 2. Display all tasks \n 3. Check the next task \n 4. Complete the next task \n 5. Quit \n')
    if option == '1':
        tasks.append(input('What task do you want to add \n'))
    elif option == '2':
        print(tasks)
    elif option == '3':
        print(tasks[listindex])
    elif option == '4':
        tasks.remove(tasks[listindex+1])
    elif option == '5':
        done = 1
    else:
        print('Please enter a Valid input')
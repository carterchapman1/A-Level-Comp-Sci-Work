import sqlite3
UserInput = input('You Have 5 options:\n1: View List \n2:Add an Item to the list \n3: Marks Something as done \n4: Sort by due date \n5: Filter by category')
connection = sqlite3.connect("Task.db")
query ="""
    SELECT * FROM Tasks
    """
if UserInput == '4':
    query += " ORDER BY 'Date Due'; "
elif UserInput == '5':
    UserCategory = input("Please pick a category")
    query += " WHERE Category = " + UserCategory + "; "
elif UserInput == '2':
    query = """
    UPDATE Tasks
    VALUES  
    """
    UserParameter = tuple(input('Please input your parameters in the form (Task,Completed,Category...)'))
    query += ""+UserParameter+";"
elif UserInput == '3':
    query = """
    UPDATE Tasks
    VALUES (Completed = '1')
    WHERE TaskId = '
    """
    UserParameter = tuple(input('Please input the TaskID of the task you would like to complete\n'))
    query += ""+UserParameter+"' ;"

print(query)
print('\nResults found:\n---------')
cursor = connection.execute(query)
for row in cursor:
    for i in range(0,6):
        print(f'| {row[i]} |',end='')
    print(f'\n')


connection.commit()
connection.close()
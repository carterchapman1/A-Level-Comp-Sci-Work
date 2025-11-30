usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("ValueError")
        return
    
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        print("IndexError")
        return 
        
    try:
        division = 301 / number
    except ZeroDivisionError:
        print('ZeroDivisionError')
        return 
    print(f"301 divided by {number} = {division}")




def login_unhandled2(usernumber):
    print("\n -- The Basic Version --\n")
    if usernumber.isdigit() == True:
        number = int(usernumber)
    else:
        print("ValueError")
        return
    
    if number < len(usernames) and number >= 0: 
        print("Welcome", usernames[number], "user number", number,".")
    else:
        print("IndexError")
        return 
        
    if number != 0:
        division = 301 / number
    else:
        print('ZeroDivisionError')
        return 
    print(f"301 divided by {number} = {division}")


class BadGuyError(Exception):
    pass

try:
    while True:
        inp = input("\nType in a number: ")
        login_unhandled(inp)
except BadGuyError:
    print("BAD GUY ERROR")    
        


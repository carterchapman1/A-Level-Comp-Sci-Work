def HashFunc(key):    
    sum = 0
    key = key
    for i in range (len(key)):
        sum += (ord(key[i])* ord(key[i]))
    Hash = sum % 523
    return Hash

list = [-1,-1] * 523 

list[HashFunc('PEN')] = ['PEN','PLUME']
list[HashFunc('CAT')] = ['CAT','CHAT']
list[HashFunc('NOW')] = ['NOW','MAINTENANT']

finished = False

while finished == False:
    userword = input('Enter a key and get the french word ')
    print(list[HashFunc(userword)][1])
    finish = input('Enter 1 if your finished using french mode ')
    if finish == '1':
        finished = True



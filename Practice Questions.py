#palindromic
list1 = []
list2 = []
middle = 0
userinput = (input("Please enter a number up to 20 digits long\n"))
halflength = len((userinput)) // 2
if halflength + halflength != len((userinput)):
    middle = userinput[halflength]
for i in range(0, halflength):
    list1.append(userinput[i])
    if halflength + halflength != len((userinput)):
        list2.append(userinput[i+halflength + 1])
    else:
        list2.append(userinput[i+halflength])
print(list1,list2, middle)
smallest = False
word = ""
list3 = []
list3 = list1
number = list3[halflength-1] 
list3[halflength-1]  = str(int(number) + 1)
for i in range(0,len(userinput)):
    word = ( word )

    


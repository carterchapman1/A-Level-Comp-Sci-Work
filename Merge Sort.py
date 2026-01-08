
def splitlist(arr:list):
    length = len(arr)//2
    arrleft = arr[0:length]
    arrright = arr[length:]
    return arrleft, arrright

def mergetwolists(arrleft:list, arrright:list):
    combinedlist = []
    i = 0
    y = 0
    for x in range(0,(len(arrleft) + len(arrright))):
        if i != len(arrleft):
            if arrleft[i] < arrright[y]:
                combinedlist.append(arrleft[i])
                i +=1
            else:
                combinedlist.append(arrright[y])
                y +=1
        else:
            combinedlist.append(arrright[y])
            y +=1
    return combinedlist

def MergeSort(Arr:list):
    if len(Arr) == 1:
        return Arr
    ArrLeft, ArrRight = splitlist(Arr)
    ArrLeft = MergeSort(ArrLeft)
    ArrRight = MergeSort(ArrRight)
    return mergetwolists(ArrLeft, ArrRight)


Array = [0,44,42,55]

print(MergeSort(Array))


    
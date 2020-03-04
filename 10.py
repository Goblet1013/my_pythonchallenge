

lastN = list('111221')
nextN = []
for i in range(5,31):
    flag = 0
    for j in range(0,len(lastN)):
        flag+=1
        if j == len(lastN) - 1:
            nextN.append(str(flag))
            nextN.append(lastN[j])
        elif lastN[j] != lastN[j+1]:
            nextN.append(str(flag))
            nextN.append(lastN[j])
            flag = 0
    lastN = nextN
    nextN = []
    print(i,len(''.join(lastN)))

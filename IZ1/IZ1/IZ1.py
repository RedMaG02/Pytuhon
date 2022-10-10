def iz1(path):

    inputFile = open(path,'r')
    inpList1 =[]

    for i in range(int(inputFile.readline())):
        line = inputFile.readline()
        strList = line.split()
        inpList1.append((int(strList[0]),int(strList[1])))


    sortedList1 = sorted(inpList1, key = lambda x: (x[0], abs(x[0]-x[1])))


    finalList = []

    for i in range(len(sortedList1)-1):
        if(not(sortedList1[i+1][0]>=sortedList1[i][0] and sortedList1[i+1][1]<= sortedList1[i][1])):
            finalList.append(sortedList1[i])
            break

    #print(sortedList1)

    for i in range(1,len(sortedList1)):

        if(i == (len(sortedList1)-1)):

            if(finalList[len(finalList)-1][1]<= sortedList1[i][0]):

                finalList.append(sortedList1[i])
        else:

            if((finalList[len(finalList)-1][1]<= sortedList1[i][0]) and not(sortedList1[i+1][0]>=sortedList1[i][0] and sortedList1[i+1][1]<= sortedList1[i][1])):

                finalList.append(sortedList1[i])

    print(len(finalList))

iz1('J:/Pytuhon/IZ1/IZ1/13a.txt')
iz1('J:/Pytuhon/IZ1/IZ1/13b.txt')
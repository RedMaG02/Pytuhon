#10(5)
#n = int(input())
#m = int(input())

#nset = set()
#mset = set()

#for i in range(n):
#    nset.add(int(input()))
#for i in range(m):
#    mset.add(int(input()))

#bothSet = nset & mset
#onlyAnyaSet = nset - mset
#onlyBoryaSet = mset - nset

#print(len(bothSet))
#for i in bothSet:
#    print(i)
    
#print(len(onlyAnyaSet))
#for i in onlyAnyaSet:
#    print(i)
    
#print(len(onlyBoryaSet))
#for i in onlyBoryaSet:
#    print(i)



#11(6)
stringList = []
n = int(input())
for i in range(n):
    stringList += input().split()
wordDictionary = dict()

for word in stringList:
    if word in wordDictionary:
        wordDictionary[word] += 1
    else:
        wordDictionary[word] = 1

pairList =[]
for word,i in wordDictionary.items():
    pairList.append((-i,word))

sortedList = sorted(pairList)
for i,word in sortedList:
    print(word)



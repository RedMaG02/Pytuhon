#10(6)
#n = int(input())
#string = ''
#
#for i in range(n):
#    string += ' ' + input()
#
#stringList = string.split()
#wordSet = set(stringList)
#
#print(len(wordSet))


#10(9)
n = int(input())
setList =[]

for i in range(n):
    tempSet = set()
    for j in range(int(input())):
        tempSet.add(input())
    setList.append(tempSet)
    tempSet.clear

intersectionSet = setList[0]
unionSet = set()

for sets in setList:
    intersectionSet &= sets
    unionSet = unionSet.union(sets)

print(len(intersectionSet))
for word in intersectionSet:
    print(word)

print(len(unionSet))
for word in unionSet:
    print(word)
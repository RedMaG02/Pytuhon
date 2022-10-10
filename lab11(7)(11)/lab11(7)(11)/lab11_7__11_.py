#11 7
n = int(input())

country = dict()

for i in range(n):
    str = input()
    strlist = str.split()
    temp = strlist[0]
    strlist.pop(0)
    for words in strlist:
        country[words] = temp
        

m = int(input())
cities = []

for i in range(m):
    cities.append(input())

for city in cities:
    print(country[city])


#11 11
tree = dict()

n = int(input())

entry = input().split()

tree[entry[1]] = 0
tree[entry[0]] = 1

for i in range(n-2):
    newEntry = input().split()
    tree[newEntry[0]] = tree[newEntry[1]] + 1


treeList = sorted(tree.items())

print(treeList)

#9
#Alexei Peter_1
#Anna Peter_1
#Elizabeth Peter_1
#Peter_11 Alexei
#Peter_111 Anna
#Paul_1 Peter_111
#Alexander_1 Paul_1
#Nicholaus_1 Paul_1


import math
#1(2)
#h = int(input('h = '))
#b = int(input('b = '))
#p = (1/2) * b *h
#print('p = ',p)



#2(4)
#year = int(input('year = '))
#if year%400 == 0:
#    print('YES')
#elif year%4 == 0 and year%100 != 0:
#    print('YES')
#else:
#    print('NO')



#3(16)
#r = int(input('r = '))
#k = int(input('k = '))
#p = int(input('p = '))

#newp = p/100 + 1
#s = r*100 + k
#newk = round(s * newp)
#newr = newk//100

#print('r = ',newr,' k = ',newk)


#4(10)
#n = int(input())
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(j,end='')
#    print()



#5(2)
#mystr = input('str = ')
#k = mystr.count(' ') + 1
#print(k)
    

#6(11)
#a0 = int(input())
#a1 = a0
#k = 0
#while a1!=0:
#    a1 = int(input())
#    if a1>a0:
#        k+=1
#    a0 = a1
#print(k)



#7(2)
#a = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6]
#k = 0
#for i in range(1,len(a)):
#    if a[i]!=a[i-1]:
#        k+=1
#print('k = ',k)



#8(6)
#def fib(n):
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)

#n = int(input('n = '))
#print(fib(n))


#9(2)
n = int(input('n = '))
a = []
for i in range(n):
    a.append(['.'] * n)

for i in range(n):
    for j in range(n):
        if i == int(n/2):
            a[i][j] = '*'
        elif j == int(n/2):
            a[i][j] = '*'
        elif i == j:
            a[i][i] = '*'
        elif i == (n-j-1):
            a[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(a[i][j],' ',end='')
    print()
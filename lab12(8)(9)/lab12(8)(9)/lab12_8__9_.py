#12(8)
n = 1
sumN = 0

while True:
    try:
        n = input()
        numericN = float(n)
        sumN = sumN + numericN
        print(sumN)
    except:
        if (len(n)==0): break
        else:
             print('input must be int or float')


#12(9)

numberToWordDict ={1: '����', 2:'���', 3: '���', 4: '������', 5:'����'}
WordToNumberDict ={'����':1, '���':2, '���':3, '������':4, '����':5}

while True:
    try:
        word = input()
        wordInt = int(word)
        print(numberToWordDict[wordInt])
    except:
        try:
            print(WordToNumberDict[word])
        except:
            if (len(word)==0): break
            else:
                print('this item does not exist in dictionary')
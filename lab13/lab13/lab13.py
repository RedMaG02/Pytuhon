class Cat():
    name = ''
    color = ''
    weight = ''

    def Meow(self):   
        print(self.name, "says meow")


#barsikCat = Cat()
#barsikCat.name = 'Barsik'
#barsikCat.color = 'Black'
#barsikCat.weight = 6
#barsikCat.Meow()

class Animal():
    name=''

    def __init__(self,name):
        self.name = name
        print(self.name, "was born!")

    def Eat(self):
        print("Nyam Nyam")

    def GetName(self):
        return self.name

    def SetName(self, name):
        self.name = name

    def MakeNoise(self):
        print(self.name,"says grrr")

#johnnyCrocodile = Animal("Johnny")

#print("animal name: ",johnnyCrocodile.GetName())
#johnnyCrocodile.SetName("Ivan")

#johnnyCrocodile.Eat()
#johnnyCrocodile.MakeNoise()

class StringVar():
    word =''

    def __init__(self, word):
        self.word = word
    
    def SetString(self, newWord):
        self.word = newWord
        
    def GetString(self):
        return self.word

#myString = StringVar('MyString')
#print(myString.GetString())
#myString.SetString('NotMyString')
#print(myString.GetString())

class Point():
    x = 0
    y = 0

    def __init__(self, myTuple ):
        x,y = myTuple
        self.x = x
        self.y = y

    def SetX(self, x):
        self.x = x

    def GetX(self):
        return self.x

    def SetY(self, y):
        self.y = y

    def GetY(self):
        return self.y

    def GetPoint(self):
        return (self.x, self.y)


class CoolerCat(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)
        print("The cat was born")

    def MakeNoise(self):
        print(self.name,"says MEOW")

#megaBarsik = CoolerCat('Barsik')
#megaBarsik.MakeNoise()

class Dog(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)
        print("The dog was born")

    def MakeNoise(self):
        print(self.name,"says GAV")

megaBarsik = CoolerCat('Barsik')
megaBarsik.MakeNoise()
megaBarsik.Eat()
drujokTheDog = Dog('Drujok')
drujokTheDog.MakeNoise()
drujokTheDog.Eat()
barbosTheDog = Dog('Barbos')
barbosTheDog.MakeNoise()
barbosTheDog.Eat()
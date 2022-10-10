class MySet():

    mySet = set()

    def __init__(self,inList):
        self.mySet = set(inList)

    def AddElem(self, element):
        self.mySet.add(element)

    def DelElem(self, element):
        self.mySet.remove(element)

    def Intersec(self, set):
        self.mySet = self.mySet.intersection(set.mySet)

    def Diff(self, set):
        self.mySet = self.mySet.Difference(set.mySet)
        
    def Union(self, set):
        self.mySet = self.mySet.Union(set.mySet)

    def NewIntersec(self, set):
        newSet = MySet()
        newSet.mySet = self.mySet.intersection(set.mySet)
        return newSet

    def NewDiff(self, set):
        newSet = MySet()
        newSet.mySet = self.mySet.Difference(set.mySet)
        return newSet
        
    def NewUnion(self, set):
        newSet = MySet()
        newSet.mySet = self.mySet.Union(set.mySet)
        return newSet



class SetModule:
    def __init__(self,setA:set, setB:set):
        self.setA = setA
        self.setB = setB

    def get_setA(self):
        return self.setA
    
    def set_setA(self,newSet: set):
        self.setA = newSet
    
    def get_setB(self):
        self.setB

    def set_setB(self,newSet: set):
        self.setB = newSet


    def get_union(self):
        return self.setA.union(self.setB)
    
    def intersection(self):
        ...

    def difference(self):
        ... 


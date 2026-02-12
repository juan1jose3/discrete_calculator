class Discrete_calculator:
    def __init__(self,SetModule):
        self.SetModule = SetModule

    def getUnion(self):
        self.SetModule.get_union(self.SetModule.get_setA(),self.SetModule.get_setB())
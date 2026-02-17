class My_set:
    def __init__(self):
        self.current_set = None

    def get_current_set(self):
        return self.current_set
    
    def set_current_Set(self,newSet: set):
        self.current_set = newSet


    



    def union(self,other_set):
        return self.current_set.union(other_set.get_current_set())
    
    def intersection(self,other_set):
        return self.current_set.intersection(other_set.get_current_set())

    def difference(self,other_set):
        return self.current_set.difference(other_set.get_current_set())
    
    def is_a_subset(self,other_set):
        return self.current_set.issubset(other_set.get_current_set())
        

    def add_to_set(self,value):
        if self.current_set == None:
            self.current_set = set()
        self.current_set.add(value)



class school:
    List_grade=[]
    def __init__(self,name,address):
        self.name=name
        self.address=address
    @classmethod    
    def addgrade(cls,_grade):
       cls.List_grade.append(_grade)
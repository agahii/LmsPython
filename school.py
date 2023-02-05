import student
class school:
   mystudent=[]
   def __init__(self,name,address):
        self.name=name
        self.address=address
@classmethod
def addstudent( cls,s1):
        cls.mystudent.append(s1)
        








import student
class school:
   List_Students=[]
   List_grades=[]
   def __init__(self,name,address):
        self.name=name
        self.address=address
@classmethod
def addstudent( cls,s1):
        cls.List_Students.append(s1)
        
@classmethod    
def addgrade(cls,_grade):
    cls.List_grades.append(_grade)



        








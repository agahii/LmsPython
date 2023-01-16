import uuid
class Subject:

    def __init__(self,_subjectname: str):
         if not isinstance(_subjectname, str):
            raise TypeError("subject must be string ")
         self.id=uuid.uuid4()
         self.subjectname=_subjectname

    def updatesubject(self,subjectname):
        self.subjectname=subjectname 



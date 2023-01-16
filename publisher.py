import uuid
class Publisher:

    def __init__(self,_publishername: str): 
         if not isinstance(_publishername, str):
            raise TypeError("publishername must be string")
         
         self.id=uuid.uuid4()
         self.publishername=_publishername

    def updatepublisher(self,publishername):
        self.publishername=publishername
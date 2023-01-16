
import uuid

class Author:
    def __init__ (self,_authorname: str):
        if not isinstance(_authorname, str):
            raise TypeError("Author name must be string ")
        self.id =uuid.uuid4()  
        self.authorName=_authorname

    def updateAuthor(self,_authorname):
        self.authorName = _authorname


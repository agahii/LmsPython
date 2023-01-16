import uuid
import author
import subject
import language
import publisher
class Book:

    

    def __init__(self,_title:str,_author : author.Author,_subject : subject.Subject,_totalpages:int,_barcode:str,_language:language.language,_publisher:publisher.Publisher):
        
        if not isinstance(_totalpages, int):
            raise TypeError("Total page must be integer")
        if not isinstance(_title, str):
            raise TypeError("titlename must be string")
        if not isinstance(_barcode, str):
            raise TypeError("Barcodename must be string")  
        if not isinstance(_author,author.Author):
            raise TypeError("Author must be author")  
        if not isinstance(_subject,subject.Subject):
            raise TypeError("Subject must be subject") 
        if not isinstance(_language,language.language):
            raise TypeError("language must be language")    
        if not isinstance(_publisher,publisher.Publisher):
            raise TypeError("publisher must be publisher") 


        self.title=_title
        self.author=_author
        self.id=uuid.uuid4() 
        self.subject=_subject
        self.total=_totalpages
        self.barcode=_barcode
        self.language=_language
        self.publisher=_publisher
        self.isissued= False
        self .isdiscard=False
        





        









        
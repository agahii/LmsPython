import model.book as book
class liabrary:
    book_shelve=[]
    def __init__(self,_libraryname: str):
        self.libraryname=_libraryname
    


    @classmethod
    def addbook(cls,_book): 
        if not isinstance(_book,book.Book):
            raise TypeError("book must be book")
        for x in cls.book_shelve:
            if x.title==_book.title:
                raise TypeError ("book with " +  _book.title  + " title already exist")
        cls.book_shelve.append(_book)
         
         
    @classmethod      
    def issuebook(cls,barcode):
     for x in cls.book_shelve:
            if(x.barcode ==barcode):
                x.isissued=True
    @classmethod
    def returnbook(cls,barcode):
        for a in cls.issuedbook:
            if barcode==a.barcode:
                print('Book Found')
                
    @classmethod
    def discardbook (cls,barcode):
        for a in cls.book_shelve:
             if (a.barcode==barcode):
                a.isdiscard=True
                
                











        
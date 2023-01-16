import  author
import publisher
import language
import subject
import book
import liabrary


myauthor=author.Author("john keats")
mysubject=subject.Subject("maths")
mylanguage=language.language("english")
mypublisher=publisher.Publisher("harry smith")
l1=liabrary.liabrary("kzl liabrary")

b1=book.Book("bfg",myauthor,mysubject,7876,"123",mylanguage,mypublisher)

#l1.addbook()

#print(len(l1.book_shelve))
l1.addbook(b1)

myauthor=author.Author("ayesha")
mysubject=subject.Subject("english")
mylanguage=language.language("urdu")
mypublisher=publisher.Publisher("john keats")
b2=book.Book("anne with an e",myauthor,mysubject,100,"124",mylanguage,mypublisher)
l1.book_shelve.append(b2)


myauthor=author.Author("ayesha")
mysubject=subject.Subject("english")
mylanguage=language.language("urdu")
mypublisher=publisher.Publisher("john keats")
b3=book.Book("harry potter",myauthor,mysubject,345,"34",mylanguage,mypublisher)
l1.book_shelve.append(b3)
print(len(l1.book_shelve))
l1.discardbook("124")
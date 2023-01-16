class language:

    def __init__(self,_languagename: str):
        if not isinstance(_languagename, str):
            raise TypeError("language name must be string ")
        self.languagename=_languagename

    def updatelanguage(self,languagename):
        self.languagename=languagename



             


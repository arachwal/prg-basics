class EBook:
    def __init__(self, title='GoT', author='me', numberofpages=420):
        self.title=title
        self.author=author
        self.numberofpages=numberofpages
        self.currentpage=1
        self.isopen=False
    
    def BookStatus(self):
        if self.isopen==False:
            print("the book is closed! you must open it first!")
        else:
            print(f"title: {self.title}")
            print(f"author: {self.author}")
            print(f"Number of Pages: {self.numberofpages}")
            print(f"Current page: {self.currentpage}")
    
    def openbook(self):
        self.isopen=True 

    def closebook(self):
        self.isopen=False   

    def read(self,pagestoread):
        if not self.isopen:
            return
        
        if self.currentpage + pagestoread > self.numberofpages:
            print('there arent this many pages in the book!,'
            ' going back to page 1')
        elif self.currentpage + pagestoread < 1:
            print("you can't go into negative pages!, " 
            "going back to page 1")
        else:
            self.currentpage+=pagestoread
        




ebook=EBook()
ebook.openbook()
ebook.BookStatus()
ebook.read(21)
ebook.BookStatus()


        
        
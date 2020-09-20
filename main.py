class Library:
    def __init__(self,listOfBooks,libraryName):
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        self.lendList = {}
        Library.addBooksinDictionary(self)

    def displayBooks(self):
        print(f"Books available in {self.libraryName}'s Library are : ")
        for index,bookname in enumerate(self.listOfBooks):
            print(f"{index + 1} : {bookname}")

    def addBooksinDictionary(self):
        for book in self.listOfBooks:
            self.lendList[book] = None
        

    def lendBook(self, book, lender):
        if book in self.listOfBooks:
            if self.lendList[book] is None:
                self.lendList[book] = lender
                print("Book Lending Successful.")
            else:
                print(f"Sorry This book has already been lended by {self.lendList[book]}.")
        else:
            print("The book is not available in our Library.")

    def returnBook(self, bookname):
        if bookname in self.listOfBooks:
            if self.lendList[bookname] is not None:
                self.lendList.pop(bookname)
            else:
                print("Book is already available in here. No one has lended it yet")
        else:
            print("That's not our Book.")

    def donateBook(self, bookname):
        self.listOfBooks.append(bookname)
        self.lendList[bookname] = None

    def removeBook(self, bookname):
        if bookname in self.listOfBooks:
            self.listOfBooks.remove(bookname)
            self.lendList.pop(bookname)
            print("Updated list of Books: ")
            for index,book in enumerate(self.listOfBooks):
                print(f"{index + 1} : {book}")

def design():
    print("------------------------MENU---------------------")
    print("1.Display Available Books \n2.Lend a Book\n3.Return a Book\n4.Donate a Book\n5.Remove a Book")
    print("0 to Exit.")

if __name__ == '__main__':
    libraryName = "Charan's Library World"
    lst = [
        "A Song of Ice and Fire","Spirituality",
        "Hindutva - The way of living", "Sanathan Dharm",
        "Lord of the Rings", "Archie's"
    ]
    Library = Library(lst,libraryName)
    design()
    while True:
        design()
        query = int(input("What do you want?: "))
        if query == 1:
            Library.displayBooks()
        
        elif query == 2:
            Library.displayBooks()
            indexOfBook = int(input("Enter the Book Code: "))
            lName = input("Enter your Name: ")
            try:
                Library.lendBook(Library.listOfBooks[indexOfBook-1] ,lName)
            except:
                print("The Book is not available in our Library.")
            #print("Book lending Successful.")

        elif query == 3:
            bookname = input("Enter the Book Name: ")
            Library.returnBook(bookname)

        elif query == 4:
            bookname = input("Enter the Book Name: ")
            Library.donateBook(bookname)
            Library.displayBooks()

        elif query == 5:
            Library.displayBooks()
            indexOfBook = int(input("Enter the Book Code: "))
            try:
                Library.removeBook(Library.listOfBooks[indexOfBook-1])
                print("Updated List of Books: ")
                Library.displayBooks()
            except:
                print("We dont have that book so you cannot remove it. ")

        elif query == 0:
            print(f"Okay Exiting {libraryName}")
            print("Thanks for having your time here.")
            break

        else:
            print("Wrong Choice: Enter Again.")
        

class CollectionBook:
    # index 0 = Book Name   ,   index 1 = Book Author Name , index 2 = Book Publication year
    list_Book = []
    def CollectionBook_init_(self):
        print("Constructor call")

    def default_AddingBooks(self):
        self.list_Book.append({"Book Name": "The Christmas Pig", "Author Name": "JK Rowling", "Publication year": "2015"})
        self.list_Book.append({"Book Name": "The Pig", "Author Name": "K Row", "Publication year": "2016"})
        self.list_Book.append({"Book Name": "The Christmas", "Author Name": "J ling", "Publication year": "2017"})
        self.list_Book.append({"Book Name": "The Cry Pig", "Author Name": "JK Row", "Publication year": "2018"})
        self.list_Book.append({"Book Name": "Whereabouts", "Author Name": "Jhumpa Lahiri", "Publication year": "2020"})

    def addBook(self):
        book_Name = input("Enter Book Name: ")
        book_Author = input("Enter Book Author Name : ")
        book_Publication_Year = input("Enter Book Publication_year : ")
        temp_list = {"Book Name": book_Name, "Author Name": book_Author, "Publication year": book_Publication_Year}
        self.list_Book.append(temp_list)

obj = CollectionBook()
obj.default_AddingBooks()
print(obj.list_Book)
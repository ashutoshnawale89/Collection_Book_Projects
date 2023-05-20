class CollectionBook:

    list_Book = []
    def CollectionBook_init_(self):
        self.list_Book = self.list_Book
        print("Constructor call")

    def addBook(self):
        book_Name = input("Enter Book Name: ")
        book_Author = input("Enter Book Author Name : ")
        book_Publication_Year = input("Enter Book Publication_year : ")
        temp_list = [book_Name, book_Author, book_Publication_Year]
        self.list_Book.append(temp_list)

obj = CollectionBook()
obj.addBook()
obj.addBook()
print(obj.list_Book)
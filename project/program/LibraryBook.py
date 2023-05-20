class CollectionBook:

    list_book = []
    def CollectionBook_init_(self):
        self.list_book = self.list_book
        print("Constructor call")

    def addBook(self):
        book_Name = input("Enter Book Name: ")
        self.list_book.append(book_Name)

obj = CollectionBook()
obj.addBook()
obj.addBook()
print(obj.list_book)
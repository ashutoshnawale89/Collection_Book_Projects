from project.program.Student import StudentUser


class CollectionBook:
    # index 0 = Book Name   ,   index 1 = Book Author Name , index 2 = Book Publication year
    list_Book = []
    borrow_Book =[]
    def __init__(self):
        self.list_Book.append({"Book Name": "The Christmas Pig", "Author Name": "JK Rowling", "Publication year": "2015", "Quantity": 25})
        self.list_Book.append({"Book Name": "The Pig", "Author Name": "K Row", "Publication year": "2016", "Quantity": 25})
        self.list_Book.append({"Book Name": "The Christmas", "Author Name": "J ling", "Publication year": "2017", "Quantity": 25})
        self.list_Book.append({"Book Name": "The Cry Pig", "Author Name": "JK Row", "Publication year": "2018", "Quantity": 25})
        self.list_Book.append({"Book Name": "Whereabouts", "Author Name": "Jhumpa Lahiri", "Publication year": "2020", "Quantity": 25})

    def addBook(self):
        book_Name = input("Enter Book Name: ")
        book_Author = input("Enter Book Author Name : ")
        book_Publication_Year = input("Enter Book Publication_year : ")
        book_quantity = int(input("Enter the Qty of Books: "))
        temp_list = {"Book Name": book_Name, "Author Name": book_Author, "Publication year": book_Publication_Year, "Quantity" : book_quantity}
        self.list_Book.append(temp_list)

    def seachByAuthorName(self, authorName):
        for i in self.list_Book:
            if authorName == i["Author Name"]:
                print(i)
                return
        print("Search by Author Name Data Not Found ..........!!  ")

    def seachByBookName(self, bookName):
        for i in self.list_Book:
            if bookName == i["Book Name"]:
                print(i)
                return
        print("Search By Book Name Data Not Found ..........!!  ")

    def borrowBook(self,name,age,bookName):
        for i in self.list_Book:
            temp_bookName = ''
            temp_authorName = ''
            temp_publicationYear = ''
            temp_qty = 0

            if bookName == i["Book Name"]:
                temp_bookName = i["Book Name"]
                temp_authorName = i["Author Name"]
                temp_publicationYear = i["Publication year"]
                temp_qty = i["Quantity"] - 1
                self.borrow_Book.append({"Name":name, "Age":age, "Book Name": temp_bookName, "Author Name": temp_authorName, "Publication year": temp_publicationYear, "Quantity" : 1})
                self.list_Book.remove(i)
                self.list_Book.append({"Book Name": temp_bookName, "Author Name": temp_authorName, "Publication year": temp_publicationYear, "Quantity" : temp_qty})
                print("Book is successfully Borrowing......")
                return
        print("Search By Book Name Data Not Found ..........!!  ")






obj = CollectionBook()
obj.seachByAuthorName("K Row")
obj.seachByBookName("The Pig")
obj.borrowBook("Kunal Pandey",25,"The Pig")
print(obj.borrow_Book)
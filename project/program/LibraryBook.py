from project.program.BooksNotAvailableException import BooksNotAvaliableException
from project.program.StudentData import StudentData
from project.program.UserExceptionHandle import UserExceptionHandle


class CollectionBook():
    # index 0 = Book Name   ,   index 1 = Book Author Name , index 2 = Book Publication year
    list_Book = []
    borrow_Book =[]
    list_StudentData = []
    def __init__(self):
        self.list_Book.append({"Book Name": "The Christmas Pig", "Author Name": "JK Rowling", "Publication year": "2015", "Quantity": 25})
        self.list_Book.append({"Book Name": "The Pig", "Author Name": "K Row", "Publication year": "2016", "Quantity": 4})
        self.list_Book.append({"Book Name": "The Christmas", "Author Name": "J ling", "Publication year": "2017", "Quantity": 25})
        self.list_Book.append({"Book Name": "The Cry Pig", "Author Name": "JK Row", "Publication year": "2018", "Quantity": 25})
        self.list_Book.append({"Book Name": "Whereabouts", "Author Name": "Jhumpa Lahiri", "Publication year": "2020", "Quantity": 25})

    def addBook(self):
        try:
            book_Name = input("Enter Book Name: ")
            book_Author = input("Enter Book Author Name : ")
            book_Publication_Year = input("Enter Book Publication_year : ")
            book_quantity = int(input("Enter the Qty of Books: "))
            temp_list = {"Book Name": book_Name, "Author Name": book_Author, "Publication year": book_Publication_Year, "Quantity" : book_quantity}
            self.list_Book.append(temp_list)
        except Exception:
            print("Exception Occurs : User not enter data in  valid format")

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
        try:
            count = len(self.list_StudentData)
            for j in self.list_StudentData:
                if j["Name"] == name and j["Age"] == age:
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
                            if i["Quantity"] != 0:
                                self.borrow_Book.append({"Name":name, "Age":age, "Book Name": temp_bookName, "Author Name": temp_authorName,
                                                     "Publication year": temp_publicationYear, "Quantity" : 1})
                                self.list_Book.remove(i)
                                self.list_Book.append({"Book Name": temp_bookName, "Author Name": temp_authorName, "Publication year": temp_publicationYear, "Quantity" : temp_qty})
                                print("Book is successfully Borrowing......")
                                return
                            else:
                                print("The Book is Not Available at this time in library...")
                                raise BooksNotAvaliableException

                    print("Search By Book Name Data Not Found ..........!!  ")
                    return
                count = count -1
            if count == 0:
                print("User Not register in library records............!")
                raise UserExceptionHandle
        except UserExceptionHandle:
            print("Exception Occurs : User is not Register ......Please Register then borrow books")
        except BooksNotAvaliableException:
            print("Exception occurs : Book not available in library........ Please visit after some days")

    def returnBook(self,name,age,bookName):
        temp_bookName = ''
        temp_authorName = ''
        temp_publicationYear = ''
        temp_qty = 0
        for i in self.borrow_Book:
            if name == i["Name"]:
                if age == i["Age"]:
                    if bookName == i["Book Name"]:
                        temp_bookName = i["Book Name"]
                        temp_authorName = i["Author Name"]
                        temp_publicationYear = i["Publication year"]
                        temp_qty = 1
                        self.borrow_Book.remove(i)
                        break

        if temp_qty == 1:
            for j in self.list_Book:
                if temp_bookName == j["Book Name"]:
                    qty = j["Quantity"] + temp_qty
                    self.list_Book.remove(j)
                    self.list_Book.append({"Book Name": temp_bookName, "Author Name": temp_authorName,
                                           "Publication year": temp_publicationYear, "Quantity": qty})
                    print("Successfully Return book...........")
        else:
            print("The User/Student Not borrowing",bookName," book")

    def trackAvailabilityBook(self):
        for i in self.list_Book:
            if 0 < i["Quantity"]:
                print(i["Book Name"],"Avalability : Yes")
            else:
                print(i["Book Name"], "Avalability : No")

    def displayBorrowedBook(self):
        for i in self.borrow_Book:
            print("Book Name: ",i["Book Name"]," Borrowe by: ",i["Name"])

    def addStudent(self):
        obj1 = StudentData()
        if len(self.list_StudentData) == 0:
            temp_list = obj1.list_StudentData
            for i in temp_list:
                self.list_StudentData.append(i)
        else:
            self.list_StudentData.clear()
            obj1.addStudentData()
            temp_list = obj1.list_StudentData
            for i in temp_list:
                self.list_StudentData.append(i)




obj = CollectionBook()
obj.addStudent()

obj.seachByAuthorName("K Row")
obj.seachByBookName("The Pig")
obj.borrowBook("Kunal Pandey",25,"The Pig")
obj.borrowBook("Kushal",25,"The Pig")
obj.borrowBook("Nikita",26,"The Pig")
obj.borrowBook("Yogesh",25,"The Pig")
obj.borrowBook("Ritesh",24,"The Pig")
print(obj.list_Book)
print(obj.borrow_Book)
obj.trackAvailabilityBook()
obj.returnBook("Kunal Pandey",25,"The Pig")
obj.returnBook("Kushal",25,"The Pig")
print(obj.borrow_Book)
print(obj.list_Book)
obj.displayBorrowedBook()
obj.addStudent()
print(obj.list_StudentData)



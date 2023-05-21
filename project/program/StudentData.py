class StudentData:
    list_StudentData = []

    def __init__(self):
        self.list_StudentData.append({"Name":"Yogesh", "Age":25, "ID Number":112233})
        self.list_StudentData.append({"Name":"Nikita", "Age":26, "ID Number":112244})
        self.list_StudentData.append({"Name":"Ritesh", "Age":22, "ID Number":155233})
        self.list_StudentData.append({"Name":"Yogita", "Age":28, "ID Number":112883})

    def addStudentData(self):
        try:
            name = input("Enter Name of Student: ")
            age = int(input("Enter the age : "))
            Id = int(input("Enter the id number"))
            self.list_StudentData.append({"Name":name, "Age": age,"ID Number":Id})
        except Exception:
            print("User Enter Wrong Data ...........!")

    def printStudentList(self):
        print(self.list_StudentData)

obj1 = StudentData()
obj1.printStudentList()

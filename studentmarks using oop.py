class all_students():
    def __init__(self,):
        self.studentslist={}
    def insert_student(self):
        while True:
            global original
            global marks
            name=input("enter student name: ")
            marks=int(input("enter student marks: "))
            if not name.isalpha():
                print("name can not include numbers or special characters")
            else:
                if marks>100 or marks<0:
                    print("marks can not be a negative or over 100")
                else:
                    original=name
                    self.studentslist.update({name.lower():marks})
                    break
    def remove_student(self):
        n=input("enter name of student u want to remove: ")
        if n.lower() in self.studentslist:
            self.studentslist.pop(n.lower())
            print(n," has been removed")
        else:
            print(f"student not found, maybe wrong spelling was entered, you wrote({n})")
    def search_student(self):
        n=input("enter name of student you want to search for: ")
        if n.lower() in self.studentslist:
            print(f"student found ({original}) and their grades are{marks}")
        else:
            print(f"student not found, maybe wrong spelling was entered, you wrote ({n})")
    def update_student(self):
        n=input("enter name of student u want to update: ")
        if n.lower() in self.studentslist:
            while True:
                m=int(input("which details would you like to update?\n1.name\n2.marks\n: "))
                if m==1:
                    while True:
                        marks2=self.studentslist[n.lower()]
                        new=input("enter new name: ")
                        if not new.isalpha():
                            print("name can not include special characters")
                        else:
                            self.studentslist[n.lower()]=marks2
                            self.studentslist.pop(n.lower())
                            self.studentslist.update({new.lower():marks2})
                            print(f"student {n} has been updated to {new}")
                        break
                elif m==2:
                    while True:
                         new=int(input("enter new marks: "))
                         if new>100 or new<0:
                             print("marks can not be negative or over 100")
                         else:
                             self.studentslist[n.lower()]=new
                             print(f"student {n} marks has been updated to {new}")
                         break
                break
        else:
            print(f"student not found, maybe wrong spelling was entered, you wrote ({n})")


system=all_students()
running=True    
while running==True:
    print("====Students Of School XYZ====")
    print("1.Insert Student")
    print("2.Remove Student")
    print("3.Search for Student")
    print("4.Update a Student")
    print("5.View all students")
    print("6.Exit")
    while True:
        choice=(input("what would you like to do? (1-6): "))
        if choice.isdigit():
                choice2=int(choice)
                match choice2:
                    case 1:
                        system.insert_student()
                        break
                    case 2:
                        system.remove_student()
                        break
                    case 3:
                        system.search_student()
                        break
                    case 4:
                        system.update_student()
                        break
                    case 5:
                        print(system.studentslist)
                        break
                    case 6:
                        print("bye")
                        running=False
                        break
                    case _:
                        print("pick something between 1-6")
                        break
        else:
            print("enter a number between 1-6")
    




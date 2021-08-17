#student management system
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade
    def show(self):
        print(self.name,self.age,self.grade)

p1=Student("Jack",22,'90')
print(p1.name)   #acessing name using p1 object
p1.show()

p2=Student("Ram",20,'80')
p2.show()          ##acessing name using p2 object
print(p1.get_grade())
print(p2.get_grade())

print(p1.__dict__)    ##using dictionary format
print(p2.__dict__)

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students=max_students
        self.students = []
    def add_student(self,student):
        if(len(self.students)< self.max_students):
            self.students.append(student)
            return True
        return False


c1=Course("Gokul",2)

print(c1.add_student(p1))
c1=Course("Ram",2)
print(c1.add_student(p2))



class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
       

    def Showdata(self):
        print("Player " + self.name)
        print("Salary = {} pound per week".format(self.salary))
        print("Department of {}".format(self.department))

    def getIncome(self) :
        return self.salary*12
    
    def __str__(self):
        return ('Name {} , Department = {} , Salary = {} ,Income = {}'.format(self.name,self.department,self.salary,self.getIncome()))

# คลาสลูก
class Engineering(Employee):

    __department = "Engineering"
    def __init__(self, name, salary):
        super().__init__(name, salary, Engineering.__department)



class Doctor(Employee):

    __department = "Doctor"
    def __init__(self, name, salary):
        super().__init__(name, salary, Doctor.__department)


# เรียกใช้งาน
eng = Engineering("Jiravat", 50000)
print(eng.__str__())
doc = Doctor("Mind", 25000)
# มันจะไปเรียก __str__ ให้อยุ่แล้ว เพราะฉะนั้นไม่ได้ต้องเขียน__str__() ก็ได้
print(doc)
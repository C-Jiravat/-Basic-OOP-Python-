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
    def __init__(self, name, salary,skill):
        super().__init__(name, salary, Engineering.__department)
        self.skill = skill
    def Showdata(self):
        super().Showdata()
        print('Skill : {}'.format(self.skill))
        print('####################')

class Doctor(Employee):

    __department = "Doctor"

    def __init__(self, name, salary,experience):
        super().__init__(name, salary, Doctor.__department)
        self.experience  =  experience

    def Showdata(self):
        super().Showdata()
        print('Experience : {}'.format(self.experience))
        print('################')


# เรียกใช้งาน
eng = Engineering("Jiravat", 50000,'Python')
eng.Showdata()
doc = Doctor("Mind", 25000,12)
# มันจะไปเรียก __str__ ให้อยุ่แล้ว เพราะฉะนั้นไม่ได้ต้องเขียน__str__() ก็ได้
doc.Showdata()
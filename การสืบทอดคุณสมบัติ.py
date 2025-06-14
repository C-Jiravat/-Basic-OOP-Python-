class Employee :
    def __init__(self,name,salary,department) :
        self.name = name
        self.salary = salary
        self.department = department
        

    def _Showdata(self) :
        print("Player " + self.name)
        print("Salary = {} pound per week".format(self.salary))
        print('Department of {}'.format(self.department))


# การสร้าง class ลูก 

class Engineering(Employee) :
    __department = 'Engineering'
    def __init__(self,name,salary) :
        # super() แทน class แม่
        super().__init__(name,salary,self.__department)
        # Class แม่เรียกคำสั่งเอง 
        super()._Showdata()

class Doctor(Employee) :
    __department = 'Doctor'
    def __init__(self,name,salary) :
        super().__init__(name,salary,self.__department)
        

eng = Engineering('Jiravat',75000)
# Class ลุกเรียกใช้ method ของ class แม่
#eng._Showdata()
doc = Doctor('Mind',25000)
doc._Showdata()




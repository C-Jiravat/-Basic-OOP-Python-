class Employee:
    # Class variable สามารถเรียกใช้งานโดยไม่ต้องผ่าน object
    _MinSalary = 10000
    _MaxSalary = 50000
    def __init__(self,name,salary) :
        # instance variable ต้องสร้าง object ถึงจะสามารถเรียกได้
        self._name = name
        self._salary = salary
     
    def _ShowData(self) :
        print("Player " + self.getName())
        print("Salary = {} pound per week".format(self.getSalary()))


emp1 = Employee('Mos',50000)
# Class varibale
print('Minsalary :',Employee._MinSalary)
# Instance variable
print('Name :',emp1._name)

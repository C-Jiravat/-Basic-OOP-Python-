print('Hello')
print("Jiravat")
# การสร้าง Constructor 
class Employee:
    # _ is protected สามารถเข้าถึงแค่ใน class ของตัวมันเอง และ class ที่ถูกสือบทอด
    # __ is private สามารถเข้าถึงเฉพาะ class ของตัวเองเท่านั้น
    
    # Private function
    def __init__(self,name,salary) :
        # Protected parameter
        self._name = name
        self.__salary = salary
        self.__ShowData()
        
    def __ShowData(self) :
        print("Employee Name :{}  \nSalary = {} $".format(self._name,self.__salary))
    
# จะเห็นว่าสามารถแก้ไข self_name ได้เพราะมันเป็น Protected 
#  แต่ salary ไม่สามารถแก้ไขไได้เพราะเป็น Private 
emp1 = Employee('Mos',50000)
emp1._name = 'Jiravat'
emp1.__salary = 20000


def showdata() :
    pass


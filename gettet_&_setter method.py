class Employee:
  
    def __init__(self,name,salary) :
        self.__name = name
        self.__salary = salary
     
    def _ShowData(self) :
        # จะเห็นได้ว่าเราสมารถแก้ไข ค่าที่เป็น Private ได้แล้ว
        print("Player " + self.getName())
        print("Salary = {} pound per week".format(self.getSalary()))

    # setter medthod ใช้แก้ไขค่าใน Private ได้
    def setName(self,newname) :
        self.__name = newname
    
    def setSalary(self,newsalary) :
        self.__salary = newsalary

    # getter method ใช้เรียกค่าใน Private ได้
    def getName(self) :
        return self.__name
    
    def getSalary(self) :
        return self.__salary
    
emp1 = Employee('Mos',50000)
emp1.setSalary(64550)
emp1.setName('Supanut')
emp1._ShowData()

# การสร้าง Class
class Employee:

    # สร้าง Method
    def details(self) :
        print('Run Method')
        
    # สร้าง Attribute
    def information(self,name,salary) :
        self.name = name
        self.salary = salary
        print("Employee Name :{}  \nSalary = {} $".format(self.name,self.salary))
        
# การสร้างวัตถุ
emp1 = Employee()
emp1.information('Mos',50000)

emp2 = Employee()
emp2.information('Bank',16000)


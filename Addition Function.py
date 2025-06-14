# การสร้าง Constructor 
class Employee:
    # ทำงานทันทีโดยไม่ได้ต้องสั่งใช้กำหนดพวก Parameter ใน Class
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

    def ShowData(self) :
        print("Employee Name :{}  \nSalary = {} $".format(self.name,self.salary))
    
# การสร้างวัตถุ
emp1 = Employee('Mos',50000)
emp2 = Employee('Bank',20000)

# isinstance เช็คว่าemp1 อยู่ใน Class Employee ไทม
print(isinstance(emp1,Employee))

# dir แสดง attribute ทั้งหมดใน class นั้นๆ 
print(dir(Employee))

# ใช้แสดงว่า emp1 อยุ่ใน class ไหน
print(emp1.__class__)
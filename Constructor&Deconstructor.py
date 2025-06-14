# การสร้าง Constructor 
class Employee:
    # ทำงานทันทีโดยไม่ได้ต้องสั่งใช้กำหนดพวก Parameter ใน Class
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

    def ShowData(self) :
        print("Employee Name :{}  \nSalary = {} $".format(self.name,self.salary))
    
    # ทำงานหลังสิ้นสุด Class ไว้คืนค่าRam ให้ระบบ
    def __del__(self) :
        print('End Class')

# การสร้างวัตถุ
emp1 = Employee('Mos',50000)
# สามารถเข้าไปเปลี่ยนค่าได้เพราะยังไม่ได้ห่อหุ้ม
emp1.salary = 10**6
emp1.ShowData()

emp2 = Employee('Bank',20000)
emp2.ShowData()
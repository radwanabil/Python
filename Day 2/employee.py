from db import database
from config import config
handler = database(config).connect()
class Employee:
    employees = []
    def __init__(self, age, first_name,last_name,department,salary):
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      self.department = department
      self.salary = salary
      Employee.employees.append(self)
      handler.insert(
            f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`) VALUES (%s, %s, %s, %s, %s)",
            (self.first_name, self.last_name,
             self.age, self.department, self.salary)
        )
    def fire(self):
       Employee.employees.remove(self)
       handler.remove(
          f"delete from `employee` where `first_name`= %s and `last_name` = %s",(self.first_name,self.last_name)
          )
    
    def transfer(self,department):
       self.department = department
       handler.update(
          f"update `employee` set `department` = %s where `first_name` = %s", (self.department, self.first_name)
       )
    def show(self):
      print("Employee name:",self.first_name, self.last_name)
      print("Employee age:",self.age)
      print("Employee department:",self.department)
      print("Employee salary:",self.salary)

    @staticmethod
    def List_employees():
       employees = handler.get_all_records(
          f"select * from employee where `managed_dept` IS NULL"
       )
       print("ALL EMPLOYEES")
       print("--------------------------------------------------------")
       for employee in employees:
            print("Employee name:",employee[1], employee[2])
            print("Employee age:",employee[3])
            print("Employee department:",employee[4])
            print("Employee salary:",employee[5])
            print("--------------------------------------------------------")
       
       

# e1 = Employee(25, "rima", "nabil", "IT", 50000)
# e1.transfer("Pharmacy")
# e1.show()
# Employee.List_employees()
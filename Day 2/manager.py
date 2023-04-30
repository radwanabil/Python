from db import database
from employee import Employee
from config import config
handler = database(config).connect()
class Manager(Employee):
    def __init__(self, age, first_name,last_name,department,salary,managed_dept):
        super().__init__(age,first_name, last_name,department, salary)
        self.managed_dept = managed_dept
        handler.update(
        f"update `employee` set managed_dept =%s where first_name= %s",
        (self.managed_dept, self.first_name)
        )
    @staticmethod
    def List_managers():
       managers = handler.get_all_records(
          f"select * from employee where `managed_dept` IS NOT NULL"
       )
       print("ALL MANAGERS")
       print("--------------------------------------------------------")
       for manager in managers:
            print("Manager name:",manager[1], manager[2])
            print("Manager age:",manager[3])
            print("Manager department:",manager[4])
            print("Manager salary: confidential")
            print("--------------------------------------------------------")
      
       

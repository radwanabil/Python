from employee import Employee
from manager import Manager


def menu():
    flag = True
    while flag:
        print("Please select an operation:")
        print("Add Employee: (enter 1)")
        print("Add Manager: (enter 2)")
        print("List all Employees: (enter 3)")
        print("List all Managers: (enter 4)")
        print("to Exit: (enter 5)")
        value = input()
        if value == "1":
            data = get_employee_data()
            Employee(*data)
        elif value == "2":
            data = get_manager_data()
            Manager(*data)
        elif value == "3":
            Employee.List_employees()
        elif value == "4":
            Manager.List_managers()
        elif value == "5":
            flag = False


def get_employee_data():
    first_name = input("Enter First Name: \n")
    last_name = input("Enter Last Name: \n")
    age = int(input("Enter Age: \n"))
    department = input("Enter Department: \n")
    salary = float(input("Enter Salary: \n"))
    return [age,first_name, last_name, department, salary]


def get_manager_data():
    data = get_employee_data()
    managed_dept = input("Enter the managed department: \n")
    data.append(managed_dept)
    return data


menu()
# Day2 Python course in ITI
# Employee and Manager Classes

This project creates two classes, `Employee` and `Manager`, with various attributes and methods to manage employee data in a company. The classes are designed to be used through a command-line interface menu.

## Employee Class

### Attributes
- First Name
- Last Name
- Age
- Department
- Salary

### Methods
- `__init__(self, first_name, last_name, age, department, salary)`: Constructor method that assigns values to the instance attributes and adds the created object to the shared list and the employee table in the database.
- `transfer(self, new_department)`: Method to change employee department and update the database record.
- `fire(self)`: Method to remove the employee from the shared list and delete its record from the database.
- `show(self)`: Method to print all employee data.
- `List_employees()`: Class method to select all employees and print their data.

## Manager Class

### Attributes
- First Name
- Last Name
- Age
- Department
- Salary
- Managed_department

### Methods
- `__init__(self, first_name, last_name, age, department, salary, managed_department)`: Constructor method that assigns values to the instance attributes and adds the created object to the shared list and the employee table in the database.
- `transfer(self, new_department)`: Method to change employee department and update the database record.
- `fire(self)`: Method to remove the employee from the shared list and delete its record from the database.
- `show(self)`: Method to print all manager data (except the salary, which is printed as "confidential").
- `List_managers()`: Class method to select all managers and print their data.

## How to Use

To use the program, run the following command:
- `python menu.py`


You will then be presented with a menu with various options to add, transfer, fire, or list employees and managers. Enter the corresponding letters to run the desired operation. For example, to add a new employee, enter "a".

At any time, you can exit the program by entering "q" in the menu.

## Dependencies

This project requires the following dependencies:
- Python 3
- MySQL




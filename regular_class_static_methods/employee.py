
class Employee:

    # class veriable
    numOfEmployees = 0
    # can be a class and instance veriable
    raiseAmount = 1.04
    
    # constractor method
    def __init__(self, firstName, lastName, salary):

        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + "." + lastName + "@company.com"
        self.salary = salary
        Employee.numOfEmployees += 1
        print('Number Of employees: {} \n'.format(Employee.numOfEmployees))
    
    @classmethod
    def fromString(cls, empStr):
        firstName, lastName, salary = empStr.split("-")
        return cls(firstName, lastName, salary)

    # this is a class method this takes class as an argument not the instance
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    @staticmethod
    def is_week_day(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return "week day"
        return "Not week day"




    def raiseSalary(self):
        self.salary = self.salary * self.raiseSalary

    def printEmployeeInfo(self):
        self.printFullName()
        self.printEmail()
        self.printSalary()

    def printFullName(self):
        print('Full Name: {} {}'.format(self.firstName, self.lastName))
    
    def printEmail(self):
        print('Email: {} '.format(self.email))

    def printSalary(self):
        print('Salary: {} \n'.format(self.salary))

    


emp1 = Employee("Debasish", "Sarker", 50000)
emp1.printEmployeeInfo()

emp2 = Employee("John", "Cena", 100000)
emp2.printEmployeeInfo()

# creating an employee from string
empStr = "Van-Dijk-100000"
emp3 = Employee.fromString(empStr)
emp3.printEmployeeInfo()

#using the static method
import datetime
date = datetime.date(2020, 8, 21)

print(Employee.is_week_day(date))

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

print('After changhing the raise amount using emp1:')
emp2.raiseAmount = 1.05

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

print('After changhing the raise amount using class method:')
Employee.setRaiseAmount(1.07)

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)



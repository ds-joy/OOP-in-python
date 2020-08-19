
class Employee:

    # class veriable
    numOfEmployees = 0
    # can be a class and instance veriable
    salaryRaise = 1.04
    
    # constractor method
    def __init__(self, firstName, lastName, salary):

        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + "." + lastName + "@company.com"
        self.salary = salary
        Employee.numOfEmployees += 1
        print('Number Of employees: {} \n'.format(Employee.numOfEmployees))

    def raiseSalary(self):
        self.salary = self.salary * self.salaryRaise


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

# here salary raise will be used as an class veriable
emp1.raiseSalary()
emp1.printEmployeeInfo()

# here salaryRaise becomes an instance veriable
emp2.salaryRaise = 1.05
emp2.raiseSalary()
emp2.printEmployeeInfo()


print(emp1.__dict__)
emp1.salaryRaise = 1.05
print(emp1.__dict__)



class Employee:

    # class veriable
    numOfEmployees = 0
    
    # constractor method
    def __init__(self, firstName, lastName, salary):

        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + "." + lastName + "@company.com"
        self.salary = salary
        Employee.numOfEmployees += 1

    def printEmployee(self):
        self.printFullName()
        self.printEmail()
        self.printSalary()
    
    def printFullName(self):
        print('Full Name: {} {}'.format(self.firstName, self.lastName))
    
    def printEmail(self):
        print('Email: {} '.format(self.email))

    def printSalary(self):
        print('Salary: {} '.format(self.salary))


print(Employee.numOfEmployees)
emp1 = Employee("Debasish", "Sarker", 50000)
emp1.printEmployee()
print(Employee.numOfEmployees)


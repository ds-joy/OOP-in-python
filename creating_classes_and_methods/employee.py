class Employee:

    # constractor
    def __init__(self, firstName, lastName, salary):

        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.email = firstName + "." + lastName + "@company.com"

    # class method
    def printEmployeeDetails(self):
        
        print('Full Name: {} {}'.format(self.firstName, self.lastName))
        print('Email: {}'.format(self.email))
        print('Salary: {}'.format(self.salary))

    

# instance object

emp1 = Employee("Debasish", "Sarker", 40000)
emp1.printEmployeeDetails()
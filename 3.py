class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display_company(self):
        print(f"Company: {self.company_name}")

class Employee(Person, Company):
    def __init__(self, name, company_name, designation):
        Person.__init__(self, name)
        Company.__init__(self, company_name)
        self.designation = designation

    def display_employee_info(self):
        self.display_name()
        self.display_company()
        print(f"Designation: {self.designation}")

# Example usage
employee = Employee("Ravi Sakariya", "Sakariya The Developement Lab", "Software Engineer")
employee.display_employee_info()

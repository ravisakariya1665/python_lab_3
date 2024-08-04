class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

# Example usage
employee = Employee("Ravi sakariya", "2024-11-07", "Software Engineer", 70000)
employee.display_info()

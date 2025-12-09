from employee import Employee

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(emp.display_info())
            print(emp.calculate_paycheck())
            
def main():
    my_company = Company("Tech Solutions")
    
    # Create employees
    emp1 = Employee("Alice", "Johnson", 60000)
    emp2 = Employee("Bob", "Lee", 55000)
    
    # Add employees to the company
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    
    # Display all employees
    my_company.display_employees()
    
main()
from employee import Employee, SalaryEmployee, HourlyEmployee


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(print(emp.fname, emp.lname))
        print("------------------")
        
    def pay_employees(self):
        print(f"Paying employees of {self.name}")
        for emp in self.employees:
            print(f"Paying {emp.fname} {emp.lname}:\n${emp.calculate_paycheck():,.2f}")
            print("------------------")
            
def main():
    my_company = Company("Tech Solutions")
    
    # Create employees
    emp1 = SalaryEmployee("Alice", "Johnson", 60000)
    emp2 = HourlyEmployee("Bob", "Lee", 36, 8)
    
    # Add employees to the company
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    
    # Display all employees
    my_company.display_employees()
    my_company.pay_employees()
    
main()
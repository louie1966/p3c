class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.fname} {self.lname}, Salary: € {self.salary}"
    
    def calculate_paycheck(self, periods=12):
        self.periods = periods
        return self.salary / periods  # Assuming bi-monthly paychecks

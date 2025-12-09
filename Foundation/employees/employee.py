class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self, periods=12):
        self.periods = periods
        return self.salary / periods  # Assuming bi-monthly paychecks


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate, hours_worked):
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked  # Assuming bi-monthly paychecks

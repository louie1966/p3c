employee1 = {"name": "Ji-Soo", "age": 38, "position": "developer", "salary": 1200}
employee2 = {"name": "Lauren", "age": 44, "position": "tester", "salary": 1000}

def init_employee(name, age, position, salary):
    return {"name": name, "age": age, "position": position, "salary": salary}

def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] * (percent / 100)

def employee_info(employee):
    print( f"{employee['name']} is a {employee['position']} earning {employee['salary']} USD")
    
employees = [employee1, employee2]

employee3 = init_employee("Carlos", 29, "manager", 1500)
employees.append(employee3)

increase_salary(employee2, 20)

for e in employees:
    employee_info(e)
   

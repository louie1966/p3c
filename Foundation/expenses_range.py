total = 0
expenses = []
amount = int(input("How many days of expenses do you want to enter? "))

for i in range(amount):
    expenses.append(float(input(f"Enter expense for day {i+1}: ")))

total = sum(expenses)
avg = total / amount

print(f"Total expenses for the week: ${total} (${avg} per day on average)")

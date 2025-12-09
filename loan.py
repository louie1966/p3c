money_owed = float(input("How much money do you owe, in dollars?\n"))  # $50,000
apr = float(input("What is the annual interest rate of the loan?\n"))  # 3%
payment = float(input("How much will you pay off each month in dollars?\n"))  # $1,000
months = int(input("How many months do you want to see results for?\n"))  # 12

monthly_rate = apr / 100 / 12

for i in range(months):
    # Calculate the interest to pay
    interest_paid = money_owed * monthly_rate
    
    # Add in intrest
    money_owed += interest_paid
    
    if money_owed < payment:
        payment = money_owed
        print("Last payment:", payment)
        print(f"Loan paid off in {i+1} months!")
        break
    
    # Make payment
    money_owed -= payment

    print('Paid', payment ,'of which', interest_paid, 'was interest',end=' ' )
    print('and now owe', money_owed)

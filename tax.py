amount = 9.5
tax = 0.06
total = amount + amount*tax
if total > 10:
    print(total)
elif total <= 10 and total > 0:
    print(f"Tax due: {total - amount}")
else:
    print("No tax due")
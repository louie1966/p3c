def addition(a, b):
    return a + b

def main():    
    num1 = float(input('Enter your first number:\n'))
    num2 = float(input('Enter your second number:\n'))
    result = addition(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

main()
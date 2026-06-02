a = float(input('enter number: '))
b = float(input('enter number: '))
operation = input("choose an operation: ")

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
elif operation == '**':
    print(a ** b)
else:
    print("Invalid operation")
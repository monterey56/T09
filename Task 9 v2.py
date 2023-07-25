import os

def write_to_file(content):
    with open("calculations.txt", 'a') as f:
        f.write(content + "\n")

def perform_operation(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == 'x':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            print("Cannot divide by zero.")
            return None
    else:
        print("Unsupported operation.")
        return None

def read_from_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return None

    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        a, operation, b = line.split()
        a, b = int(a), int(b)
        result = perform_operation(a, b, operation)
        if result is not None:
            print(f"{a} {operation} {b} = {result}")

def calculator():
    while True:
        mode = input("Enter '1' to perform calculation, '2' to read from file, '3' to exit: ")

        if mode == '1':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            operation = input("Enter operation (+, -, x, /): ")

            result = perform_operation(a, b, operation)
            if result is not None:
                print(f"{a} {operation} {b} = {result}")
                write_to_file(f"{a} {operation} {b} = {result}")
        elif mode == '2':
            filename = input("Enter filename: ")
            read_from_file(filename)
        elif mode == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid mode.")

calculator()

import os

def write_to_file(content):
    with open("calculations.txt", 'x') as f:
        f.write(content + "\n")

#operations and zero division error
def perform_operation(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == 'x':
        return x * y
    elif operation == '/':
        if y != 0:
            return x / y
        else:
            print("Cannot divide by zero.")
            return None
    else:
        print("Unsupported operation.")
        return None
    
#read from txt file
def read_from_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return None

    with open(filename, 'r') as f:
        lines = f.readlines()

#expected format for equations to be read
    for line in lines:
        x, operation, y = line.split()
        x, y = int(x), int(y)
        result = perform_operation(x, y, operation)
        if result is not None:
            print(f"{x} {operation} {y} = {result}")

#take user inputs and store as variables
def calculator():
    while True:
        mode = input("Enter '1' to perform calculation, '2' to read from file, '3' to exit: ")

        if mode == '1':
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            operation = input("Enter operation (+, -, x, /): ")

            result = perform_operation(x, y, operation)
            if result is not None:
                print(f"{x} {operation} {y} = {result}")
                write_to_file(f"{x} {operation} {y} = {result}")
        elif mode == '2':
            filename = input("Enter filename: ")
            read_from_file(filename)
        elif mode == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid mode.")

calculator()
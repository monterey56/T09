#ask the user to make input in a basic calculator program (2 numbers and an operation)
#display the answer to the equation
#every equation written by the user should be input to a text file
#use defensive programming to handle unexpected events and user inputs

# define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#take user inputs as variables
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        #perform calculations and print result
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation")
            continue

        print(f"{num1} {op} {num2} = {result}")

        #write result to calculations.txt
        with open("calculations.txt", "a") as f:
            f.write(f"{num1} {op} {num2} = {result}\n")

        """
        ask user if they want to perform operations from a text file.
        if true, open text file and perform calculations. if n, exit program
        if y, read text file and perform calculations. exit and return errors
        if incorrectly formatted or file does not exist
        """
        read_file = input("Do you want to read equations from a file? (y/n): ")
        if read_file.lower() == "n":
            break
        elif read_file.lower() == "y":
            while True:
                try:
                    file_name = input("Enter file name: ")
                    with open(file_name) as f:
                        for line in f:
                            try:
                                num1, op, num2, eq_result = line.split()
                                result = 0
                                if op == "+":
                                    result = add(float(num1), float(num2))
                                elif op == "-":
                                    result = subtract(float(num1), float(num2))
                                elif op == "*":
                                    result = multiply(float(num1), float(num2))
                                elif op == "/":
                                    result = divide(float(num1), float(num2))
                                else:
                                    print(f"Invalid operation in line: {line}")
                                    continue
                                print(f"{line.strip()} = {result}")
                            except ValueError:
                                print(f"Invalid line format: {line}")
                    break
                except FileNotFoundError:
                    print(f"File not found: {file_name}")
                    continue
    except ValueError:
        print("Invalid input")
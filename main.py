print("Available operations:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

operation = input("Enter the operation (+, -, *, /): ")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _:
        print("^_____^")
        exit()

print(num1, operation, num2, "=", result)
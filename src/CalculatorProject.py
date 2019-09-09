def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("Pick Function")
print("+ - Addition")
print("- - Subtraction")
print("* - Multiplication")
print("/ - Division")

Function = input("Pick Operation (+ or - or * or /):")

message1 = int(input("First Figure: "))
message2 = int(input("Second Figure: "))

if Function == '+':
    print(message1, "+", message2, "=", add(message1,message2))

elif Function == '-':
     print(message1, "-", message2, "=", subtract(message1, message2))

elif Function == '*':
     print(message1, "*", message2, "=", multiply(message1, message2))

elif Function == '/':
     print(message1, "/", message2, "=", divide(message1, message2))
else:
    print("Wrong Operation Input")

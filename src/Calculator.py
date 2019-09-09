## This program perform simple calculation operations
print("This Program Perform simple Mathematics Calculations \n")
print("For Addition select 1 ")
print("For Multiplication select 2 ")
print("For Modulus select 3 ")
print("For Division select 4 ")
print("To raise a number to the power of another select 5 \n")
n = input("Please select appropriate numbers: \n")

option = int(n)

if(option == 1):
    first_Number = int(input("Please type in the first number for Addition:- "))
    second_Number = int(input("Plase type in the second number for Addition:- "))
    result = first_Number+second_Number
    print(result)
elif(option == 3):
    first_Number = int(input("Please type the first number for modulus:- "))
    second_Number = int(input("Please type in the second number for modulus:- "))
    result = first_Number%second_Number
    print(result)
elif(option == 2):
    first_Number = int(input("Please type the first number for multiplication:- "))
    second_Number = int(input("Please type in the second number for multiplication:- "))
    result = first_Number * second_Number
    print(result)
elif(option == 4):
    first_Number = int(input("Please type the first number for Division:- "))
    second_Number = int(input("Please type in the second number for Division:- "))
    result = first_Number/second_Number
    print(result)
elif (option == 5):
    first_Number = int(input("Please type the number:- "))
    second_Number = int(input("Please type in the power:- "))
    result = first_Number**second_Number
    print(result)
else:
    print("whoops wrong operation selection!!!!")
    print("Thank you very much \n")
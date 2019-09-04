## This program perform simple calculation operations
print("This Program Perform simple Mathematics Calculations \n")
print("For Addition select 1 : ")
print("For Multiplication select 2 : \n")
n = input("Please select appropriate numbers: \n")

option = int(n)

if(option == 1):
    first_Number = int(input("Please type in the first number for Addition:- "))
    second_Numbber = int(input("Plase type in the second number for Addition:- "))
    result = first_Number+second_Numbber
    print(result)
else:
    print("whoops wrong operation selection!!!!")
    print("Thank you very much \n")
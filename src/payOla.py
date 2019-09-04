import math
# inp = input(" Please Enter Hours of working...  ")
#
# try:
#     print(inp)
#     rate = 12.50
#     hour = float(inp)
#     pay = rate * hour
#     print(pay)
# except:
#     print("please Re-run your application and put it in correct Numbers not characters...")

## range with input

inp = input("Please Enter you input from range 0.0 to 1.0...  ")
# for i in range(1,10):
#     print(i)
try:
    wel = float(inp)
    if(wel>=0.9):
        print("Your Grade is : A")
    elif():
        print("Your Grade is : B")
    elif(wel>=0.8):
        print("Your Greade is : C")
    elif(wel>=0.7):
        print("Your Greade is : D")
    elif(wel>=0.6):
        print("Your Greade is : E")
    elif (wel < 0.6):
        print("Your Greade is : F")
except:
    print("Wrong input correct number between")
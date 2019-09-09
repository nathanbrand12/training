# ### Python Program to find GCD of Two Numbers
# #
# a = float(input(" Please Enter the First Value a: "))
# b = float(input(" Please Enter the Second Value b: "))
#
# i = 1
# while (i <= a and i <= b):
#     if (a % i == 0 and b % i == 0):
#         gcd = i
#     i = i + 1
#
# print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))

# ###------------------------------------------------------------
# # Python Program to find GCD of Two Numbers
#
# num1 = float(input(" Please Enter the First Value  Num1 : "))
# num2 = float(input(" Please Enter the Second Value Num2 : "))
#
# a = num1
# b = num2
#
# while(num2 != 0):
#     temp = num2
#     num2 = num1 % num2
#     num1 = temp
#
# gcd = num1
# print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))

# ####------------------------------------------------------------------
# # Python Program to find GCD of Two Numbers
# # we are finding the GCD without using Temp variable
#
# num1 = float(input(" Please Enter the First Value  Num1 : "))
# num2 = float(input(" Please Enter the Second Value Num2 : "))
#
# a = num1
# b = num2
#
# if(num1 == 0):
#     print("\n HCF of {0} and {1} = {2}".format(a, b, b))
#
# while(num2 != 0):
#     if(num1 > num2):
#         num1 = num1 - num2
#     else:
#         num2 = num2 - num1
#
# gcd = num1
# print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))

# ####-----------------------------------------------------------------

# Python Program to find GCD of Two Numbers
#
def findgcd(num1, num2):
    if(num1 == 0):
        print("\n HCF of {0} and {1} = {2}".format(a, b, b))

    while(num2 != 0):
        if(num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

print("GCD of Two Numbers using Functions with Recursion \n")
a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

gcd = findgcd(a, b)
print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))
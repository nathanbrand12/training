import math


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print("-----------------------------------")
    print(magician + " Welcome")
    print("-----------------------------------")
    print(magician.title() + ", Nice Trick")
    print("-----------------------------------")
    print("I can't wait to see your next trick, "+ magician.title()+ ".\n") 
print("Thank you it was a great show!!!")

number = list(range(1,8))

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print(magicians[-3])
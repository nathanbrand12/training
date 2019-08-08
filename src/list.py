vehicle = ["Toyota", "Camry", "Honda", "Mazda", "BMW", "Mercedez"]

# print all list
print(vehicle)
#Print single element of a list while counting fromm left to right
print(vehicle[1])

# Print single element of a list while counting from right to the left
print(vehicle[-1])

#Print single element in a list
hey = "I love " + vehicle[1]
print(hey)

## Adding List
vehicle.append("Anything")
print(vehicle)

## Removing type of list
del vehicle[1]
print(vehicle)

## Insert into a list
vehicle.insert(0, "Mario")
print(vehicle)

# Pop an item from a list
last_vehicle =vehicle.pop()
print("This pop the last element from a list "+last_vehicle)

pop_variable = vehicle.pop(0)
print("Pop a single list element"+pop_variable+".")

#Sort a list
vehicle.sort()
print("\n Sorted lists")
print(vehicle)

vehicle.reverse()
print("\n Reverse Lists")
print(vehicle)